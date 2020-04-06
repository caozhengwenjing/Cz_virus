### 当月总额
```sql
SELECT SUM(字段) 
FROM 表名 
WHERE DATE_FORMAT( 时间字段, '%Y%m' ) = DATE_FORMAT( CURDATE( ) , '%Y%m' )

```

### 上月
```sql
SELECT SUM(字段) 
FROM 表名 
WHERE DATE_FORMAT(时间字段, '%Y %m') = DATE_FORMAT(DATE_SUB(CURDATE(), INTERVAL 1 MONTH),'%Y %m')
```


### 年总额
```sql
SELECT SUM(字段) 
FROM 表名 
WHERE  YEAR(时间字段)=YEAR(NOW()) 

```


### 去年总额
```sql
SELECT SUM(字段) 
FROM 表名 
WHERE  YEAR(时间字段)=YEAR(DATE_SUB(NOW(),INTERVAL 1 YEAR))

```


### 当年每月数据
```sql
SELECT DATE_FORMAT(时间字段, "%Y-%m")AS MONTH,SUM(money)AS totalmoney 
FROM 表名
WHERE DATE_FORMAT(时间字段, "%Y-%m-%d") >= "2020-01-01" 
GROUP BY DATE_FORMAT(时间字段, "%Y-%m")

```

### 当月每日数据
```sql
SELECT DATE_FORMAT(时间字段, "%m-%d") AS MONTH,SUM(money) AS totalmoney 
FROM 表名
WHERE DATE_FORMAT(时间字段, "%Y-%m-%d") >= "2019-01-01" AND DATE_FORMAT( 时间字段, '%Y%m' ) = DATE_FORMAT( CURDATE( ) , '%Y%m' )
GROUP BY DATE_FORMAT(时间字段, "%Y-%m-%d")

```


### 上月每天数据
```sql
SELECT DATE_FORMAT(时间字段, "%m-%d") AS MONTH,SUM(money) AS totalmoney 
FROM 表名
WHERE DATE_FORMAT(时间字段, '%Y %m') = DATE_FORMAT(DATE_SUB(CURDATE(), INTERVAL 1 MONTH),'%Y %m') 
GROUP BY DATE_FORMAT(时间字段, "%Y-%m-%d")

```


### 小于一万的个数
```sql
SELECT COUNT(*),submit_time 
FROM 表名 
WHERE 字段 < 10000  AND DATE_FORMAT( 时间字段, '%Y%m' ) = DATE_FORMAT( CURDATE( ) , '%Y%m' )

```


### 在一万到三万之间的个数
```sql
SELECT COUNT(*),submit_time 
FROM 表名 
WHERE 字段 BETWEEN 10000 AND 30000 AND DATE_FORMAT( 时间字段, '%Y%m' ) = DATE_FORMAT( CURDATE( ) , '%Y%m' )

```


### 范围汇总
```sql
SELECT mina,maxa,maxx, maxxx FROM (
(SELECT  COUNT(*)  mina FROM 表名 WHERE 字段 < 10000  AND DATE_FORMAT( 时间字段, '%Y%m' ) = DATE_FORMAT( CURDATE( ) , '%Y%m' )) AS mina ,
(SELECT  COUNT(*) maxa FROM 表名 WHERE 字段 BETWEEN 10000 AND 30000  AND DATE_FORMAT( 时间字段, '%Y%m' ) = DATE_FORMAT( CURDATE( ) , '%Y%m' )) AS  maxa,
(SELECT  COUNT(*) maxx FROM 表名 WHERE 字段 BETWEEN 30000 AND 100000  AND DATE_FORMAT( 时间字段, '%Y%m' ) = DATE_FORMAT( CURDATE( ) , '%Y%m' )) AS  maxx,
(SELECT  COUNT(*) maxxx FROM 表名 WHERE 字段 > 100000  AND DATE_FORMAT( 时间字段, '%Y%m' ) = DATE_FORMAT( CURDATE( ) , '%Y%m' ) ) AS maxxx
)
```


### 当天数据总额
```sql
SELECT SUM(字段),时间字段 FROM 表名 WHERE TO_DAYS(时间字段) = TO_DAYS(NOW())AND order_state = 2

```


### 近30天的数据
```sql
SELECT 字段,时间字段,id FROM 表名 WHERE DATE_SUB(CURDATE(), INTERVAL 14 DAY) <= DATE(时间字段)

```


### 某年某月的数据
```sql
SELECT 字段,时间字段,id FROM 表名 WHERE DATE_FORMAT (时间字段,'%Y-%m') = '2019-10' AND order_state = 2

```

### 当前这周的数据
```sql
SELECT 字段,时间字段,id FROM 表名 WHERE YEARWEEK(DATE_FORMAT(时间字段,'%Y-%m-%d')) = YEARWEEK(NOW()) 

```

### 上周的数据
```sql
SELECT 字段,时间字段,id FROM 表名 WHERE YEARWEEK(DATE_FORMAT(时间字段,'%Y-%m-%d')) = YEARWEEK(NOW())-1 

```


### 查询当前月份或任意某个月的数据()
```sql
SELECT 字段,时间字段,id FROM 表名 WHERE DATE_FORMAT(时间字段,'%Y-%m')=DATE_FORMAT(NOW(),'%Y-%m') //=后面可换为具体时间，查询任意月份的数据

```


### 查询距离当前时间6个月的数据
```sql
SELECT 字段,submit_time,id FROM 表名 WHERE submit_time BETWEEN DATE_SUB(NOW(),INTERVAL 6 MONTH) AND NOW();

```

















