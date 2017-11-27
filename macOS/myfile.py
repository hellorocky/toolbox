#!/usr/bin/env python3
"""
文件上传/下载脚本(到自己的VPS中)

使用方法:
    将该文件放到PATH中,并把如下信息加入zshrc:
    alias up='python myfile.py up'
    alias down='python myfile.py down'

    up filename即可
"""
import sys
import subprocess

UPLOAD_URL = "http://rockywu.me/up/"
DOWNLOAD_URL = "http://rockywu.me/down/"

def run_cmd(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    p.wait()
    out = p.stdout.readlines()
    return p.returncode, out



if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(1)
    if sys.argv[1] in ("u", "up"):
        cmd = "curl --insecure -T {filename} {url}".format(filename=sys.argv[2], url=UPLOAD_URL)
    elif sys.argv[1] in ("d", "down"):
        cmd = "wget  --no-check-certificate {url}{filename}".format(filename=sys.argv[2], url=UPLOAD_URL)
    print("**" * 10 + DOWNLOAD_URL+sys.argv[2] + "**" * 10)
    run_cmd(cmd)
