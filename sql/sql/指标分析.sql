DELETE FROM zhubo202003_copy2 WHERE conversion_rate IS NULL AND clicks IS NULL

SELECT * FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100

符合条件个数
SELECT COUNT(id) FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100

销售额总值
SELECT SUM(unit_sales) FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100

销售均值
SELECT 
(SELECT SUM(unit_sales) FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100)
/
(SELECT COUNT(id) FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS s



销售倍数
SELECT 	id, zhi/
(SELECT   
(SELECT SUM(unit_sales) FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100)
/
(SELECT COUNT(id) FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100)    )AS xiaoshou

FROM(
(SELECT id, unit_sales zhi FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100)  AS zhi,
(SELECT   
(SELECT SUM(unit_sales) FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100)
/
(SELECT COUNT(id) FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100)    )AS jun
)

销量均值均值
SELECT 
(SELECT SUM(sales_volume) FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100)
/
(SELECT COUNT(id) FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS l



销量倍数

SELECT 	id , liang/
(SELECT   
(SELECT SUM(sales_volume) FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100)
/
(SELECT COUNT(id) FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100)    )AS xiaoliang

FROM(
(SELECT id, sales_volume liang FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100)  AS liang,
(SELECT   
(SELECT SUM(sales_volume) FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100)
/
(SELECT COUNT(id) FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100)    )AS jun
)


转化率均值
SELECT 
(SELECT SUM(conversion_rate) FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100)
/
(SELECT COUNT(id) FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS zhuan


转化率倍数
SELECT 	id , AVG(zhuan/jun) AS zhuan

FROM(
(SELECT id, conversion_rate zhuan FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100)  AS zhuan,
(SELECT   
(SELECT SUM(conversion_rate) FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100)
/
(SELECT COUNT(id) FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100)  AS jun  ) AS z
)

点击数均值
SELECT 
(SELECT SUM(clicks) FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100)
/
(SELECT COUNT(id) FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS dian


点击数倍数
SELECT 	id,category_name , AVG(dian/jun) AS dian

FROM(
(SELECT id,category_name, clicks dian FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100)  AS dian,
(SELECT   
(SELECT SUM(clicks) FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100)
/
(SELECT COUNT(id) FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100)  AS jun  ) AS d
)GROUP BY category_name ORDER   BY   dian   






SELECT 	id,category_name , dian/jun AS dian

FROM(
(SELECT id,category_name, clicks dian FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100)  AS dian,
(SELECT   
(SELECT SUM(clicks) FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100)
/
(SELECT COUNT(id) FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100)  AS jun  ) AS d
)GROUP BY category_name ORDER   BY   dian   DESC LIMIT 10 













SELECT 	id,category_name , dian/(SELECT   (SELECT SUM(clicks) FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100)/(SELECT COUNT(id) FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100)    )AS dian FROM((SELECT id,category_name, clicks dian FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100)  AS dian,(SELECT   (SELECT SUM(clicks) FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100)/(SELECT COUNT(id) FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100)    )AS jun )GROUP BY category_name ORDER   BY   dian   DESC
















