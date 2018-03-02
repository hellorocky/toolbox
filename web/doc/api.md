#### 接口域名

`ansible.office.bbobo.com`

#### 通用发送任务接口

* 接口地址

`/v1/task`

* 请求方式

`POST`

* 请求参数


```json
{
"action": "setup",
"data": {
		"ips": "192.168.1.1,192.168.1.2,192.168.1.3",
		"task_id": "123456abc",
		"task_args": {"key": "value"}
		}
}
```


#### 通用查询任务结果接口

* 接口地址

`/v1/task/123456abc`

* 请求方式

`GET`


* 返回结果

```
{
  "status_code": "0000",
  "msg": {
    "status": "已完成",
    "result": "sdfbftrhr34dfgdgfdnrnfdnfg", #base64
    "create_time": "2018-03-01 16:16:39",
    "finish_time": "2018-03-01 16:23:05"
  }
}
```

#### 健康检查接口

* 接口地址

`/status`

* 请求方式

`GET`


* 返回结果

```
{
"status": "OK",
 "score": 10
 }
```