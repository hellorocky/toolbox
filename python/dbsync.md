#### 使用举例
 

* 如果只是提供了数据库名称, 没有提供表的话, 会把这个库下面的所有表都同步过去

```bash
$mpsync -sip 127.0.0.1 -su username -spwd password -dip 目标IP  -du username -dpwd password -d 数据库名称
```

* 如果提供了数据库名称, 并且提供了1个或者多个表的名称的话就会只同步指定的表的数据

```bash
$mpsync -sip 127.0.0.1 -su username -spwd password -dip 目标IP  -du username -dpwd password -d 数据库名称 -t table1 table2 table3
```

* 如果提供了数据库, 并且只指定了1个表的名称, 这时候就可以使用SQL条件语句来同步该表的部分数据, 如下(注意条件中是单引号包含双引号):

```bash
$mpsync -sip 127.0.0.1 -su username -spwd password -dip 目标IP  -du username -dpwd password -d 数据库名称 -t table1 -w type='"Idc"'
```

* 按照id倒序10000条

```bash
$mpsync -sip rdsa5.mysql.rds.aliyuncs.com -su account -spwd GPDv -dip 10.10.20.144  -du root -dpwd xxx -d account  -t mpc_daily_score_201712 -l 10000 -w '1=1 order by id desc'
```
