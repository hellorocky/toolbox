"""gunicorn WSGI server configuration, used for production environment"""
import os
import sys
from multiprocessing import cpu_count

bind = "127.0.0.1:8082"
max_requests = 1000 # 当某个worker同时处理超过1000的时候会重启,防止内存泄漏
worker_class = 'gevent'
workers = cpu_count()
worker_connections = 100 # 同时允许最大100个连接
keepalive = 30 # HTTP的keepalive, 等待下一个请求的时间, 如果30秒没有下一次请求就会关闭这个HTTP连接
timeout = 30 # 子进程30秒内没有响应那么主进程会杀死他然后起一个新的子进程
user = "xxx"
group = "xxx"
loglevel = 'info'
#capture_output=True
#errorlog = '/log/gunicorn_error.log'
#accesslog = '/log/gunicorn_access.log'
