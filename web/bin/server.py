import os
import json
import time
import logging
import traceback

import pymysql
from flask import Flask
from flask import request

from config import config

logger = logging.getLogger(__name__)

connection = pymysql.connect(host=config.MYSQL_HOST,
                             user=config.MYSQL_USER,
                             password=config.MYSQL_PASSWD,
                             db=config.MYSQL_DB,
                             charset="utf8",
                             autocommit=True,
                             connect_timeout=5,
                             cursorclass=pymysql.cursors.DictCursor)

app = Flask(__name__)


@app.route("/v1/task", methods=["POST"])
def task():
    # 获取并校验参数
    content = request.get_json(silent=True)
    action = content.get("action", "")
    data = content.get("data")
    if not data or not isinstance(data, dict):
        return json.dumps({"status_code": "5001", "msg": "参数缺失!"}, ensure_ascii=False)

    if not (action and task_id and ips):
        return json.dumps({"status_code": "5001", "msg": "参数缺失!"}, ensure_ascii=False)

    # 插入数据库
    connection.ping(reconnect=True)
    try:
        with connection.cursor() as cursor:
            sql = "SELECT `task_id` from `task_record` WHERE `task_id`='{0}'".format(task_id)
            cursor.execute(sql)
            result = cursor.fetchone()
        if result:
            return json.dumps({"status_code": "5002", "msg": "数据库插入失败, 重复的task_id!"}, ensure_ascii=False)

        with connection.cursor() as cursor:
            sql = "INSERT INTO `task_record` (`task_id`, `ips`, `action`, `task_args`, `create_time`) VALUES ('{0}', '{1}', '{2}', '{3}', {4})".format(
                task_id, ips, action, task_args, int(time.time()))
            cursor.execute(sql)
    except Exception as e:
        logger.error(traceback.format_exc(e))
        logger.info(json.dumps(content, ensure_ascii=False))
        return json.dumps({"status_code": "5002", "msg": "数据库插入失败!"}, ensure_ascii=False)
    return json.dumps({"status_code": "0000", "msg": "任务添加成功!"}, ensure_ascii=False)


@app.route("/v1/task/<task_id>", methods=["GET"])
def get_task(task_id):
    """
    :param task_id: 唯一任务ID
    :return: {"status_code": "0000", "msg": {"status": 0, "result": "abc"}}
    """
    if task_id:
        with connection.cursor() as cursor:
            sql = "SELECT `status`, `result`, `create_time`, `finish_time` FROM `task_record` WHERE `task_id`='{0}'".format(
                task_id)
            cursor.execute(sql)
            result = cursor.fetchone()
        if not result:
            return json.dumps({"status_code": "5004", "msg": "该任务不存在"}, ensure_ascii=False)
        # 格式转化
        if result["status"] == 0:
            result["status"] = "已完成"
        elif result["status"] == 1:
            result["status"] = "未完成"
        else:
            result["status"] = "进行中"

        result["create_time"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(result["create_time"]))
        if result["finish_time"]:
            result["finish_time"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(result["finish_time"]))

        return json.dumps({"status_code": "0000", "msg": result}, ensure_ascii=False)
    else:
        return json.dumps({"status_code": "5001", "msg": "参数缺失"}, ensure_ascii=False)


@app.route("/ping", methods=["GET"])
def ping():
    """
    检查服务状态
    """
    return "OK"
