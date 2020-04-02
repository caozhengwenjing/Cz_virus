销售额正规化法
SELECT *,(zong-xiao)/(da-xiao)  FROM (
(SELECT id, commodity_information,affiliated_shop, unit_sales zong  FROM   zhubo202003_copy2  WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS zong,
(SELECT   MIN(unit_sales) xiao FROM   zhubo202003_copy2  WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) xiao,
(SELECT   MAX(unit_sales) da FROM   zhubo202003_copy2  WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) da

)


销售量正规化法
SELECT *,(zong-xiao)/(da-xiao)  FROM (
(SELECT id, commodity_information,affiliated_shop, sales_volume zong  FROM   zhubo202003_copy2  WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS zong,
(SELECT   MIN(sales_volume) xiao FROM   zhubo202003_copy2  WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) xiao,
(SELECT   MAX(sales_volume) da FROM   zhubo202003_copy2  WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) da
)


V销
SELECT *,(k.e+j.l)/2 FROM (
(SELECT *,(zong-xiao)/(da-xiao) e  FROM (
(SELECT id, commodity_information,affiliated_shop, unit_sales zong  FROM   zhubo202003_copy2  WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS zong,
(SELECT   MIN(unit_sales) xiao FROM   zhubo202003_copy2  WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) xiao,
(SELECT   MAX(unit_sales) da FROM   zhubo202003_copy2  WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) da) 
)AS k
INNER JOIN

(SELECT *,(zong-xiao)/(da-xiao) l FROM (
(SELECT id, sales_volume zong  FROM   zhubo202003_copy2  WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS zong,
(SELECT   MIN(sales_volume) xiao FROM   zhubo202003_copy2  WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) xiao,
(SELECT   MAX(sales_volume) da FROM   zhubo202003_copy2  WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) da) 
)AS j ON k.id = j.id
)


V流
SELECT *,(k.e+j.l)/2 FROM (
(SELECT *,(zong-xiao)/(da-xiao) e  FROM (
(SELECT id, commodity_information,affiliated_shop, conversion_rate zong  FROM   zhubo202003_copy2  WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS zong,
(SELECT   MIN(conversion_rate) xiao FROM   zhubo202003_copy2  WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) xiao,
(SELECT   MAX(conversion_rate) da FROM   zhubo202003_copy2  WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) da) 
)AS k
INNER JOIN

(SELECT *,(zong-xiao)/(da-xiao) l FROM (
(SELECT id, clicks zong  FROM   zhubo202003_copy2  WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS zong,
(SELECT   MIN(clicks) xiao FROM   zhubo202003_copy2  WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) xiao,
(SELECT   MAX(clicks) da FROM   zhubo202003_copy2  WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) da) 
)AS j ON k.id = j.id
) 

V销  V流  V综
SELECT k.id,k.commodity_information,k.zong,k.category_name,k.category,k.anchor,(k.e+j.l+f.v+g.h)/4 v_zong,(k.e+j.l)/2 v_xiao,(f.v+g.h)/2 V_liu FROM (
(SELECT *,(zong-xiao)/(da-xiao) e  FROM (
(SELECT id,anchor, commodity_information,affiliated_shop,category, category_name,unit_sales zong  FROM   zhubo202003_copy2  WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS zong,
(SELECT   MIN(unit_sales) xiao FROM   zhubo202003_copy2  WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) xiao,
(SELECT   MAX(unit_sales) da FROM   zhubo202003_copy2  WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) da) 
)AS k
INNER JOIN
(SELECT *,(zong-xiao)/(da-xiao) l FROM (
(SELECT id, sales_volume zong  FROM   zhubo202003_copy2  WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS zong,
(SELECT   MIN(sales_volume) xiao FROM   zhubo202003_copy2  WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) xiao,
(SELECT   MAX(sales_volume) da FROM   zhubo202003_copy2  WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) da) 
)AS j ON k.id = j.id
INNER JOIN
(SELECT *,(zong-xiao)/(da-xiao) v FROM (
(SELECT id, conversion_rate zong  FROM   zhubo202003_copy2  WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS zong,
(SELECT   MIN(conversion_rate) xiao FROM   zhubo202003_copy2  WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) xiao,
(SELECT   MAX(conversion_rate) da FROM   zhubo202003_copy2  WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) da) 
)AS f ON f.id = j.id
INNER JOIN
(SELECT *,(zong-xiao)/(da-xiao) h FROM (
(SELECT id, clicks zong  FROM   zhubo202003_copy2  WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS zong,
(SELECT   MIN(clicks) xiao FROM   zhubo202003_copy2  WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) xiao,
(SELECT   MAX(clicks) da FROM   zhubo202003_copy2  WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) da) 
)AS g ON g.id = f.id )
 ORDER   BY   v_zong   DESC  LIMIT 10
 
