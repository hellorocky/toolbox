#!/usr/bin/env python3
import os
import sys
import time
import argparse
import tempfile
import traceback
import subprocess


class MysqlDump(object):
    def __init__(self, src_ip, src_port, src_user, src_password, dest_ip, dest_port, dest_user, dest_password, dbname, table, limit, where):
        self.src_ip = src_ip
        self.src_port = src_port
        self.src_user = src_user
        self.src_password = src_password
        self.dest_ip = dest_ip
        self.dest_port = dest_port
        self.dest_user = dest_user
        self.dest_password = dest_password
        self.dbname = dbname
        self.tables = table
        self.limit = limit
        self.where = where
        print("源数据库信息: IP地址: {0}, 端口: {1}, 用户名: {2}, 密码: {3}".format(self.src_ip, self.src_port, self.src_user, self.src_password))
        print("目标数据库信息: IP地址: {0}, 端口: {1}, 用户名: {2}, 密码: {3}".format(self.dest_ip, self.dest_port, self.dest_user, self.dest_password))

    @staticmethod
    def run_cmd(cmd):
        try:
            p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")
            p.wait()
            out = p.stdout.read() #type: str
            err = p.stderr.read() #type: str
            if p.returncode != 0:
                print(err)
                sys.exit(250)
            else:
                return out
        except:
            print(traceback.print_exc())
            sys.exit(250)
        finally:
            p.kill()

    def sync_total(self):
        """同步数据库中所有的表"""
        tmpdir = tempfile.TemporaryDirectory()
        tmpdir_name = tmpdir.name
        tmp_db_path = os.path.join(tmpdir_name, self.dbname+".sql")
        dump_cmd = "mysqldump -h{0} -u{1} -P{2} -p'{3}' --default-character-set=utf8 --single-transaction -w '1=1 limit {4}' {5} > {6}".format(self.src_ip, self.src_user, self.src_port, self.src_password, self.limit, self.dbname, tmp_db_path)
        self.run_cmd(dump_cmd)
        print("数据库: {0}导出完毕!".format(self.dbname))
        createdb_cmd = "mysql -h{0} -u{1} -P{2} -p'{3}' -e 'CREATE DATABASE IF NOT EXISTS {4}'".format(self.dest_ip, self.dest_user, self.dest_port, self.dest_password, self.dbname)
        self.run_cmd(createdb_cmd)
        print("目标数据库创建成功, 正在导入...")
        restore_cmd = "mysql -h{0} -u{1} -P{2} -p'{3}' {4} < {5}".format(self.dest_ip, self.dest_user, self.dest_port, self.dest_password, self.dbname, tmp_db_path)
        self.run_cmd(restore_cmd)
        print("同步完成!")
        # 显式关闭临时目录
        tmpdir.cleanup()

    def sync_condition(self):
        tmpdir = tempfile.TemporaryDirectory()
        tmpdir_name = tmpdir.name
        tmp_db_path = os.path.join(tmpdir_name, self.tables[0]+".sql")
        if not self.where:
            self.where = "1=1"
        dump_cmd = "mysqldump -h{0} -u{1} -P{2} -p'{3}' --default-character-set=utf8 --single-transaction -w '{4} limit {5}' {6} {7} > {8}".format(self.src_ip, self.src_user, self.src_port, self.src_password, self.where, self.limit, self.dbname, self.tables[0], tmp_db_path)
        self.run_cmd(dump_cmd)
        print("数据库: {0}中的表: {1}导出成功!".format(self.dbname, self.tables[0]))
        createdb_cmd = "mysql -h{0} -u{1} -P{2} -p'{3}' -e 'CREATE DATABASE IF NOT EXISTS {4}'".format(self.dest_ip, self.dest_user, self.dest_port, self.dest_password, self.dbname)
        self.run_cmd(createdb_cmd)
        print("目标数据库创建成功, 正在导入...")
        restore_cmd = "mysql -h{0} -u{1} -P{2} -p'{3}' {4} < {5}".format(self.dest_ip, self.dest_user, self.dest_port, self.dest_password, self.dbname, tmp_db_path)
        self.run_cmd(restore_cmd)
        print("同步完成!")
        # 显式关闭临时目录
        tmpdir.cleanup()

    def sync_tables(self):
        self.where = "1=1"
        createdb_cmd = "mysql -h{0} -u{1} -P{2} -p'{3}' -e 'CREATE DATABASE IF NOT EXISTS {4}'".format(self.dest_ip, self.dest_user, self.dest_port, self.dest_password, self.dbname)
        self.run_cmd(createdb_cmd)
        print("目标数据库创建成功, 正在导入...")
        tmpdir = tempfile.TemporaryDirectory()
        tmpdir_name = tmpdir.name
        for table in self.tables:
            tmp_db_path = os.path.join(tmpdir_name, table+".sql")
            dump_cmd = "mysqldump -h{0} -u{1} -P{2} -p'{3}' --default-character-set=utf8 --single-transaction -w '{4} limit {5}' {6} {7} > {8}".format(self.src_ip, self.src_user, self.src_port, self.src_password, self.where, self.limit, self.dbname, table, tmp_db_path)
            self.run_cmd(dump_cmd)
            print("数据库: {0}中的表: {1}导出成功!".format(self.dbname, table))
            restore_cmd = "mysql -h{0} -u{1} -P{2} -p'{3}' {4} < {5}".format(self.dest_ip, self.dest_user, self.dest_port, self.dest_password, self.dbname, tmp_db_path)
            self.run_cmd(restore_cmd)
            print("数据库: {0}中的表: {1}导入成功!".format(self.dbname, table))
        print("同步完成!")
        # 显式关闭临时目录
        tmpdir.cleanup()


    def run(self):
        # 如果不指定表的话会进行该数据库的全部表的同步
        if not self.tables:
            self.sync_total()
        # 如果只指定一个表的话, 可以根据条件同步记录
        elif len(self.tables) == 1:
            self.sync_condition()
        # 既指定数据库又指定多个表, 那么会同步指定的表
        else:
            self.sync_tables()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="一下科技RDS数据库传输工具(线上到线下)!")
    parser.add_argument("-sip", "--src_ip", dest="src_ip", type=str, metavar="源IP", help="请输入源数据库IP地址", required=True)
    parser.add_argument("-sp", "--src_port", dest="src_port", default=3306, type=int, metavar="源端口", help="请输入源数据库端口号(不传默认3306)")
    parser.add_argument("-su", "--src_user", dest="src_user", type=str, metavar="源账号", help="请输入源数据库用户名称", required=True)
    parser.add_argument("-spwd", "--src_password", dest="src_password", type=str, metavar="源密码", help="请输入源数据库密码", required=True)
    parser.add_argument("-dip", "--dest_ip", dest="dest_ip", type=str, metavar="目标IP", help="请输入目标数据库IP地址", required=True)
    parser.add_argument("-dp", "--dest_port", dest="dest_port", default=3306, type=int, metavar="目标端口", help="请输入目标数据库端口号(不传默认3306)")
    parser.add_argument("-du", "--dest_user", dest="dest_user", type=str, metavar="目标账号", help="请输入目标数据库用户名称", required=True)
    parser.add_argument("-dpwd", "--dest_password", dest="dest_password", type=str, metavar="目标密码", help="请输入目标数据库密码", required=True)
    parser.add_argument("-l", "--limit", dest="limit", default=100, type=int, metavar="单个表传输几条数据", help="请输入单个表要传输的条数(默认100条)")
    parser.add_argument("-d", "--database",dest="dbname", type=str, metavar="数据库名称", help="请输入库名称", required=True)
    parser.add_argument("-t", "--table", dest="table", type=str, nargs="*", help="请输入表名, 多个以空格分隔")
    parser.add_argument("-w", "--where",dest="where", type=str, metavar="条件", help ="请输入SQL where条件")
    args = parser.parse_args()

    start = time.time()
    dump = MysqlDump(args.src_ip, args.src_port, args.src_user, args.src_password, args.dest_ip, args.dest_port, args.dest_user, args.dest_password, args.dbname, args.table, args.limit, args.where)
    dump.run()
    end = time.time()
    print("总共耗时: {0:0.2f}秒!".format(end-start))

