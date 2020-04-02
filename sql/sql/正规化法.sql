SELECT   *  FROM   zhubo202003_copy2  WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100 ORDER   BY   unit_sales   DESC LIMIT 0,1



SELECT   unit_sales  FROM   zhubo202003_copy2  WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100 ORDER   BY unit_sales ASC LIMIT 0,1

销售额最小
SELECT   MIN(unit_sales)  FROM   zhubo202003_copy2  WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100

销售额最大
SELECT   MAX(unit_sales)  FROM   zhubo202003_copy2  WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100

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






转化率正规化法
SELECT *,(zong-xiao)/(da-xiao)  FROM (
(SELECT id, commodity_information,affiliated_shop, conversion_rate zong  FROM   zhubo202003_copy2  WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS zong,
(SELECT   MIN(conversion_rate) xiao FROM   zhubo202003_copy2  WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) xiao,
(SELECT   MAX(conversion_rate) da FROM   zhubo202003_copy2  WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) da

)

点击数正规化法
SELECT *,(zong-xiao)/(da-xiao) a  FROM (
(SELECT id, commodity_information,affiliated_shop,unit_sales,category_name,category,anchor, clicks zong  FROM   zhubo202003_copy2  WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS zong,
(SELECT   MIN(clicks) xiao FROM   zhubo202003_copy2  WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) xiao,
(SELECT   MAX(clicks) da FROM   zhubo202003_copy2  WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) da
)   ORDER   BY   a   DESC LIMIT 10






销售量正规化法
SELECT id, liang_d.sales_volume,(sales_volume-s_xiao)/(x_da-s_xiao) liang_z FROM (
(SELECT  MIN(x_a) s_xiao,MAX(x_a) x_da FROM(
(SELECT id,sales_volume,IF(sales_volume>x_a,x_a,sales_volume) AS x_a ,IF(sales_volume<x_i,x_i,sales_volume) AS x_i  FROM (
(SELECT id,sales_volume FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS q,
(SELECT  e.e + e_cha.E*4 x_a FROM 
((SELECT AVG(sales_volume)  e FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS e ,
(SELECT STD(sales_volume) E FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS e_cha
)) AS w,
(SELECT  e.e - e_cha.E*4 x_i FROM 
((SELECT AVG(sales_volume)  e FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS e ,
(SELECT STD(sales_volume) E FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS e_cha
))AS a
))AS s_z
))AS xiao_zhi,
(SELECT id,sales_volume,IF(sales_volume>x_a,x_a,sales_volume) AS x_a ,IF(sales_volume<x_i,x_i,sales_volume) AS x_i  FROM (
(SELECT id,sales_volume FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS q,
(SELECT  e.e + e_cha.E*4 x_a FROM 
((SELECT AVG(sales_volume)  e FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS e ,
(SELECT STD(sales_volume) E FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS e_cha
)) AS w,
(SELECT  e.e - e_cha.E*4 x_i FROM 
((SELECT AVG(sales_volume)  e FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS e ,
(SELECT STD(sales_volume) E FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS e_cha
))AS a)
)AS liang_d
)







销售额正规化法
SELECT id, xiao_d.unit_sales,xiao_d.payment_amount,xiao_d.affiliated_shop,xiao_d.commodity_information,xiao_d.category_name,(unit_sales-s_xiao)/(x_da-s_xiao) xiao_z FROM (
(SELECT  MIN(e_a) s_xiao,MAX(e_a) x_da FROM(
(SELECT id,commodity_information, unit_sales,IF(unit_sales>e_a,e_a,unit_sales) AS e_a ,IF(unit_sales<e_i,e_i,unit_sales) AS e_i  FROM (
(SELECT id,commodity_information, unit_sales,category_name FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS q,
(SELECT  e.e + e_cha.E*4 e_a FROM 
((SELECT AVG(unit_sales)  e FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS e ,
(SELECT STD(unit_sales) E FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS e_cha
)) AS w,
(SELECT  e.e - e_cha.E*4 e_i FROM 
((SELECT AVG(unit_sales)  e FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS e ,
(SELECT STD(unit_sales) E FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS e_cha
))AS a
))AS s_z
))AS xiao_zhi,
(SELECT id,commodity_information,category_name,affiliated_shop,payment_amount, unit_sales,IF(unit_sales>e_a,e_a,unit_sales) AS e_a ,IF(unit_sales<e_i,e_i,unit_sales) AS e_i  FROM (
(SELECT id,commodity_information, unit_sales ,category_name,affiliated_shop,payment_amount FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS q,
(SELECT  e.e + e_cha.E*4 e_a FROM 
((SELECT AVG(unit_sales)  e FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS e ,
(SELECT STD(unit_sales) E FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS e_cha
)) AS w,
(SELECT  e.e - e_cha.E*4 e_i FROM 
((SELECT AVG(unit_sales)  e FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS e ,
(SELECT STD(unit_sales) E FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS e_cha
))AS a))AS xiao_d
)


转化率正规化法
SELECT id, zhuan_d.conversion_rate,(conversion_rate-s_xiao)/(x_da-s_xiao) zhuan_z FROM (
(SELECT  MIN(z_a) s_xiao,MAX(z_a) x_da FROM(
(SELECT id,conversion_rate,IF(conversion_rate>z_a,z_a,conversion_rate) AS z_a ,IF(conversion_rate<z_i,z_i,conversion_rate) AS z_i  FROM (
(SELECT id,conversion_rate FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS q,
(SELECT  e.e + e_cha.E*4 z_a FROM 
((SELECT AVG(conversion_rate)  e FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS e ,
(SELECT STD(conversion_rate) E FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS e_cha
)) AS w,
(SELECT  e.e - e_cha.E*4 z_i FROM 
((SELECT AVG(conversion_rate)  e FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS e ,
(SELECT STD(conversion_rate) E FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS e_cha
))AS a
))AS s_z
))AS xiao_zhi,
(SELECT id,conversion_rate,IF(conversion_rate>z_a,z_a,conversion_rate) AS z_a ,IF(conversion_rate<z_i,z_i,conversion_rate) AS z_i  FROM (
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
)AS zhuan_d
)



转化率正规化法
SELECT id, dian_d.clicks,(clicks-s_xiao)/(x_da-s_xiao) d_z FROM (
(SELECT  MIN(i_a) s_xiao,MAX(i_a) x_da FROM(
(SELECT id, clicks,IF(clicks>i_a,i_a,clicks) AS i_a ,IF(clicks<i_i,i_i,clicks) AS i_i  FROM (
(SELECT id,  clicks FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS q,
(SELECT e.e + e_cha.E*4 i_a FROM 
((SELECT AVG(clicks)  e FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS e ,
(SELECT STD(clicks) E FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS e_cha
)) AS w,
(SELECT  e.e - e_cha.E*4 i_i FROM 
((SELECT AVG(clicks)  e FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS e ,
(SELECT STD(clicks) E FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND payment_amount BETWEEN 0 AND 100) AS e_cha
))AS a))AS s_z
))AS xiao_zhi,
(
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
)AS dian_d
)


















