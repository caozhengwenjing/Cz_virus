SELECT  sa.id,category_name,SUM(xiaoshou+dian+zhuan+xiaoliang) AS zhibiao,SUM(xiaoshou+xiaoliang),SUM(zhuan+dian) FROM( 
(SELECT id,category_name,zhi/ jun AS xiaoshou

FROM(
(SELECT id,category_name, unit_sales zhi FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100)  AS zhi,
(SELECT   
(SELECT SUM(unit_sales) FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100)
/
(SELECT COUNT(id) FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100)   AS jun ) AS s
))AS sa
INNER JOIN

(SELECT id, dian/ jun AS dian

FROM(
(SELECT id, clicks dian FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100)  AS dian,
(SELECT   
(SELECT SUM(clicks) FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100)
/
(SELECT COUNT(id) FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100)  AS jun  ) AS d
)
)AS dian


ON dian.id =sa.id 

INNER JOIN

(SELECT id, zhuan/jun AS zhuan

FROM(
(SELECT id, conversion_rate zhuan FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100)  AS zhuan,
(SELECT   
(SELECT SUM(conversion_rate) FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100)
/
(SELECT COUNT(id) FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100)  AS jun  ) AS z
))AS zhuan
ON sa.id = zhuan.id

INNER JOIN

(SELECT id,  liang/jun AS xiaoliang

FROM(
(SELECT id, sales_volume liang FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100)  AS liang,
(SELECT   
(SELECT SUM(sales_volume) FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100)
/
(SELECT COUNT(id) FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100)  AS jun  ) AS l
)
) AS l
ON l.id = sa.id

)GROUP BY category_name ORDER   BY   zhibiao   DESC LIMIT 10