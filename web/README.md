#### 框架简介

&emsp;作为一个后端工程师, 经常会写一些内部的接口, 虽然`Flask`已经足够简单, 但是某些配置还是需要自定义的, 比如打日志, 目录结构等. 这时候打造一个自己的Web Api框架是很有必要的, 这里就简单说明一下自己的这个微型框架.

#### 适用场景

* 纯API接口
* 内部系统, 比如运维平台的部分接口

当然其它的场景都是可以的, 只是我用这个框架经常用来在以上场景, 框架会不断更新


#### 目录结构

```
├── README.md
├── bin # 业务逻辑和一些基础的函数等
│   ├── server.py
│   └── utils.py
├── conf # 各种配置文件
│   ├── config.py
│   ├── gunicorn.py
│   └── supervisord.conf
├── doc # 项目文档
│   ├── api.md
│   └── modules.md
├── log # 日志
│   └── app.log
├── manage.py # 启动入口
├── requirements.txt
└── test # 测试脚本
    └── test.py
```

#### 启动方式

* 当请求量不是很大的时候可以直接启动单进程的模式直接以如下的方式启动:

```
python manage.py
```

* 当请求量比较大的时候可以使用`gunicorn`的方式启动:

```
# 需要先进入manage.py所在的目录
gunicorn -c gunicorn.py manage:app
```


#### TODO

* 封装pymysql, 使用连接池的方式
* 启动方式选择配置文件优化