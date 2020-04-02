销售额均值
SELECT AVG(unit_sales)FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100

销售额标准差
SELECT STD(clicks)FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100


销售量均值
SELECT AVG(sales_volume)FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100

销售量标准差
SELECT STD(clicks)FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100


转化率均值
SELECT AVG(conversion_rate)FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100

转化率标准差
SELECT STD(clicks)FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100



点击数均值
SELECT AVG(clicks)FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100

点击数标准差
SELECT STD(clicks)FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100



点击率
SELECT id, clicks,IF(clicks>i_a,i_a,clicks) AS i_a ,IF(clicks<i_i,i_i,clicks) AS i_i  FROM (
(SELECT id,  clicks FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS q,
(SELECT e.e + e_cha.E*4 i_a FROM 
((SELECT AVG(clicks)  e FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS e ,
(SELECT STD(clicks) E FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS e_cha
)) AS w,
(SELECT  e.e - e_cha.E*4 i_i FROM 
((SELECT AVG(clicks)  e FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS e ,
(SELECT STD(clicks) E FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS e_cha
))AS a

)







转化率
SELECT id,conversion_rate,IF(conversion_rate>z_a,z_a,conversion_rate) AS z_a ,IF(conversion_rate<z_i,z_i,conversion_rate) AS z_i  FROM (
(SELECT id,conversion_rate FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS q,
(SELECT  e.e + e_cha.E*4 z_a FROM 
((SELECT AVG(conversion_rate)  e FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS e ,
(SELECT STD(conversion_rate) E FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS e_cha
)) AS w,
(SELECT  e.e - e_cha.E*4 z_i FROM 
((SELECT AVG(conversion_rate)  e FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS e ,
(SELECT STD(conversion_rate) E FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS e_cha
))AS a
)



测试
SELECT id,conversion_rate,IF(conversion_rate>z_a,z_a,conversion_rate) AS z_a ,IF(conversion_rate<z_i,z_i,conversion_rate) AS z_i ,
IF(conversion_rate)

 FROM (
(SELECT id,conversion_rate FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS q,
(SELECT  e.e + e_cha.E*4 z_a FROM 
((SELECT AVG(conversion_rate)  e FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS e ,
(SELECT STD(conversion_rate) E FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS e_cha
)) AS w,
(SELECT  e.e - e_cha.E*4 z_i FROM 
((SELECT AVG(conversion_rate)  e FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS e ,
(SELECT STD(conversion_rate) E FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS e_cha
))AS a
)





销售量
SELECT id,sales_volume,IF(sales_volume>x_a,x_a,sales_volume) AS x_a ,IF(sales_volume<x_i,x_i,sales_volume) AS x_i  FROM (
(SELECT id,sales_volume FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS q,
(SELECT  e.e + e_cha.E*4 x_a FROM 
((SELECT AVG(sales_volume)  e FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS e ,
(SELECT STD(sales_volume) E FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS e_cha
)) AS w,
(SELECT  e.e - e_cha.E*4 x_i FROM 
((SELECT AVG(sales_volume)  e FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS e ,
(SELECT STD(sales_volume) E FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS e_cha
))AS a
)


销售额
SELECT id, unit_sales,IF(unit_sales>e_a,e_a,unit_sales) AS e_a ,IF(unit_sales<e_i,e_i,unit_sales) AS e_i  FROM (
(SELECT id, unit_sales FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS q,
(SELECT  e.e + e_cha.E*4 e_a FROM 
((SELECT AVG(unit_sales)  e FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS e ,
(SELECT STD(unit_sales) E FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS e_cha
)) AS w,
(SELECT  e.e - e_cha.E*4 e_i FROM 
((SELECT AVG(unit_sales)  e FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS e ,
(SELECT STD(unit_sales) E FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS e_cha
))AS a
)



