SELECT *,f.id,f.commodity_information,f.category_name,ROUND(f.payment_amount,2),f.affiliated_shop, IF(ROUND((k.d_z+j.zhuan_z+f.xiao_z+g.liang_z)/4*100,2)>100,100,ROUND((k.d_z+j.zhuan_z+f.xiao_z+g.liang_z)/4*100,2))    v_zong,   IF(ROUND((f.xiao_z+g.liang_z)/2*100,2)>100,100,ROUND((f.xiao_z+g.liang_z)/2*100,2)) v_xiao , IF(ROUND((k.d_z+j.zhuan_z)/2*100,2)>100,100,ROUND((k.d_z+j.zhuan_z)/2*100,2))   V_liu FROM (
(
SELECT id,ROUND(dian_d.conversion_rate*100,2) zhuan,number_of_clicks,dian_d.anchor,dian_d.data_time, dian_d.clicks,(clicks-s_xiao)/(x_da-s_xiao) d_z FROM (
(SELECT  MIN(i_i) s_xiao,MAX(i_a) x_da FROM(
(SELECT id, clicks,IF(clicks>i_a,i_a,clicks) AS i_a ,IF(clicks<i_i,i_i,clicks) AS i_i  FROM (
(SELECT id,  clicks FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND category_name = '洗护清洁剂/卫生巾/纸/香薰' AND anchor = '薇娅' AND payment_amount BETWEEN 0 AND 100) AS q,
(SELECT e.e + e_cha.E*4 i_a FROM 
((SELECT AVG(clicks)  e FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND category_name = '洗护清洁剂/卫生巾/纸/香薰' AND anchor = '薇娅' AND payment_amount BETWEEN 0 AND 100) AS e ,
(SELECT STD(clicks) E FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND category_name = '洗护清洁剂/卫生巾/纸/香薰' AND anchor = '薇娅' AND payment_amount BETWEEN 0 AND 100) AS e_cha
)) AS w,
(SELECT  e.e - e_cha.E*4 i_i FROM 
((SELECT AVG(clicks)  e FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND category_name = '洗护清洁剂/卫生巾/纸/香薰' AND anchor = '薇娅' AND payment_amount BETWEEN 0 AND 100) AS e ,
(SELECT STD(clicks) E FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND category_name = '洗护清洁剂/卫生巾/纸/香薰' AND anchor = '薇娅' AND payment_amount BETWEEN 0 AND 100) AS e_cha
))AS a))AS s_z
)
)AS xiao_zhi,
(
SELECT number_of_clicks,conversion_rate,data_time,anchor,id, clicks,IF(clicks>i_a,i_a,clicks) AS i_a ,IF(clicks<i_i,i_i,clicks) AS i_i  FROM (
(SELECT * FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND category_name = '洗护清洁剂/卫生巾/纸/香薰' AND anchor = '薇娅' AND payment_amount BETWEEN 0 AND 100) AS q,
(SELECT e.e + e_cha.E*4 i_a FROM 
((SELECT AVG(clicks)  e FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND category_name = '洗护清洁剂/卫生巾/纸/香薰' AND anchor = '薇娅' AND payment_amount BETWEEN 0 AND 100) AS e ,
(SELECT STD(clicks) E FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND category_name = '洗护清洁剂/卫生巾/纸/香薰' AND anchor = '薇娅' AND payment_amount BETWEEN 0 AND 100) AS e_cha
)) AS w,
(SELECT  e.e - e_cha.E*4 i_i FROM 
((SELECT AVG(clicks)  e FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND category_name = '洗护清洁剂/卫生巾/纸/香薰' AND anchor = '薇娅' AND payment_amount BETWEEN 0 AND 100) AS e ,
(SELECT STD(clicks) E FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND category_name = '洗护清洁剂/卫生巾/纸/香薰' AND anchor = '薇娅' AND payment_amount BETWEEN 0 AND 100) AS e_cha
))AS a
)
)AS dian_d
)

)AS k

INNER JOIN
(

SELECT id, zhuan_d.conversion_rate,(conversion_rate-s_xiao)/(x_da-s_xiao) zhuan_z FROM (
(SELECT  MIN(z_i) s_xiao,MAX(z_a) x_da FROM(
(SELECT id,conversion_rate,IF(conversion_rate>z_a,z_a,conversion_rate) AS z_a ,IF(conversion_rate<z_i,z_i,conversion_rate) AS z_i  FROM (
(SELECT id,conversion_rate FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND category_name = '洗护清洁剂/卫生巾/纸/香薰' AND anchor = '薇娅'  AND payment_amount BETWEEN 0 AND 100) AS q,
(SELECT  e.e + e_cha.E*4 z_a FROM 
((SELECT AVG(conversion_rate)  e FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND category_name = '洗护清洁剂/卫生巾/纸/香薰' AND anchor = '薇娅'  AND payment_amount BETWEEN 0 AND 100) AS e ,
(SELECT STD(conversion_rate) E FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND category_name = '洗护清洁剂/卫生巾/纸/香薰' AND anchor = '薇娅'  AND payment_amount BETWEEN 0 AND 100) AS e_cha
)) AS w,
(SELECT  e.e - e_cha.E*4 z_i FROM 
((SELECT AVG(conversion_rate)  e FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND category_name = '洗护清洁剂/卫生巾/纸/香薰' AND anchor = '薇娅'  AND payment_amount BETWEEN 0 AND 100) AS e ,
(SELECT STD(conversion_rate) E FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND category_name = '洗护清洁剂/卫生巾/纸/香薰' AND anchor = '薇娅'  AND payment_amount BETWEEN 0 AND 100) AS e_cha
))AS a
))AS s_z
))AS xiao_zhi,
(SELECT id,conversion_rate,IF(conversion_rate>z_a,z_a,conversion_rate) AS z_a ,IF(conversion_rate<z_i,z_i,conversion_rate) AS z_i  FROM (
(SELECT id,conversion_rate FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND category_name = '洗护清洁剂/卫生巾/纸/香薰' AND anchor = '薇娅'  AND payment_amount BETWEEN 0 AND 100) AS q,
(SELECT  e.e + e_cha.E*4 z_a FROM 
((SELECT AVG(conversion_rate)  e FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND category_name = '洗护清洁剂/卫生巾/纸/香薰' AND  anchor = '薇娅'  AND payment_amount BETWEEN 0 AND 100) AS e ,
(SELECT STD(conversion_rate) E FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND category_name = '洗护清洁剂/卫生巾/纸/香薰' AND anchor = '薇娅'  AND payment_amount BETWEEN 0 AND 100) AS e_cha
)) AS w,
(SELECT  e.e - e_cha.E*4 z_i FROM 
((SELECT AVG(conversion_rate)  e FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND category_name = '洗护清洁剂/卫生巾/纸/香薰' AND anchor = '薇娅'  AND payment_amount BETWEEN 0 AND 100) AS e ,
(SELECT STD(conversion_rate) E FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND category_name = '洗护清洁剂/卫生巾/纸/香薰' AND anchor = '薇娅'  AND payment_amount BETWEEN 0 AND 100) AS e_cha
))AS a
)
)AS zhuan_d
)

)AS j ON k.id = j.id
INNER JOIN


(


SELECT id, xiao_d.unit_sales,xiao_d.payment_amount,xiao_d.affiliated_shop,xiao_d.commodity_information,xiao_d.category_name,(unit_sales-s_xiao)/(x_da-s_xiao) xiao_z FROM (
(SELECT  MIN(e_a) s_xiao,MAX(e_a) x_da FROM(
(SELECT id,commodity_information, unit_sales,IF(unit_sales>e_a,e_a,unit_sales) AS e_a ,IF(unit_sales<e_i,e_i,unit_sales) AS e_i  FROM (
(SELECT id,commodity_information, unit_sales,category_name FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND category_name = '洗护清洁剂/卫生巾/纸/香薰' AND anchor = '薇娅' AND payment_amount BETWEEN 0 AND 100) AS q,
(SELECT  e.e + e_cha.E*4 e_a FROM 
((SELECT AVG(unit_sales)  e FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND category_name = '洗护清洁剂/卫生巾/纸/香薰' AND anchor = '薇娅' AND payment_amount BETWEEN 0 AND 100) AS e ,
(SELECT STD(unit_sales) E FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND category_name = '洗护清洁剂/卫生巾/纸/香薰' AND anchor = '薇娅' AND payment_amount BETWEEN 0 AND 100) AS e_cha
)) AS w,
(SELECT  e.e - e_cha.E*4 e_i FROM 
((SELECT AVG(unit_sales)  e FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND category_name = '洗护清洁剂/卫生巾/纸/香薰' AND anchor = '薇娅' AND payment_amount BETWEEN 0 AND 100) AS e ,
(SELECT STD(unit_sales) E FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND category_name = '洗护清洁剂/卫生巾/纸/香薰' AND anchor = '薇娅' AND payment_amount BETWEEN 0 AND 100) AS e_cha
))AS a
))AS s_z
))AS xiao_zhi,
(SELECT id,commodity_information,category_name,affiliated_shop,payment_amount, unit_sales,IF(unit_sales>e_a,e_a,unit_sales) AS e_a ,IF(unit_sales<e_i,e_i,unit_sales) AS e_i  FROM (
(SELECT id,commodity_information, unit_sales ,category_name,affiliated_shop,payment_amount FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND category_name = '洗护清洁剂/卫生巾/纸/香薰' AND anchor = '薇娅' AND payment_amount BETWEEN 0 AND 100) AS q,
(SELECT  e.e + e_cha.E*4 e_a FROM 
((SELECT AVG(unit_sales)  e FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND category_name = '洗护清洁剂/卫生巾/纸/香薰' AND  anchor = '薇娅' AND payment_amount BETWEEN 0 AND 100) AS e ,
(SELECT STD(unit_sales) E FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND category_name = '洗护清洁剂/卫生巾/纸/香薰' AND anchor = '薇娅' AND payment_amount BETWEEN 0 AND 100) AS e_cha
)) AS w,
(SELECT  e.e - e_cha.E*4 e_i FROM 
((SELECT AVG(unit_sales)  e FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND category_name = '洗护清洁剂/卫生巾/纸/香薰' AND anchor = '薇娅' AND payment_amount BETWEEN 0 AND 100) AS e ,
(SELECT STD(unit_sales) E FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND category_name = '洗护清洁剂/卫生巾/纸/香薰' AND anchor = '薇娅' AND payment_amount BETWEEN 0 AND 100) AS e_cha
))AS a))AS xiao_d
)

)AS f ON f.id = j.id


INNER JOIN

(

SELECT id, liang_d.sales_volume,(sales_volume-s_xiao)/(x_da-s_xiao) liang_z FROM (
(SELECT  MIN(x_i) s_xiao,MAX(x_a) x_da FROM(
(SELECT id,sales_volume,IF(sales_volume>x_a,x_a,sales_volume) AS x_a ,IF(sales_volume<x_i,x_i,sales_volume) AS x_i  FROM (
(SELECT id,sales_volume FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND category_name = '洗护清洁剂/卫生巾/纸/香薰'  AND anchor = '薇娅' AND payment_amount BETWEEN 0 AND 100) AS q,
(SELECT  e.e + e_cha.E*4 x_a FROM 
((SELECT AVG(sales_volume)  e FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND category_name = '洗护清洁剂/卫生巾/纸/香薰' AND anchor = '薇娅' AND payment_amount BETWEEN 0 AND 100) AS e ,
(SELECT STD(sales_volume) E FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND category_name = '洗护清洁剂/卫生巾/纸/香薰' AND anchor = '薇娅' AND payment_amount BETWEEN 0 AND 100) AS e_cha
)) AS w,
(SELECT  e.e - e_cha.E*4 x_i FROM 
((SELECT AVG(sales_volume)  e FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND category_name = '洗护清洁剂/卫生巾/纸/香薰' AND anchor = '薇娅' AND payment_amount BETWEEN 0 AND 100) AS e ,
(SELECT STD(sales_volume) E FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活' AND category_name = '洗护清洁剂/卫生巾/纸/香薰' AND anchor = '薇娅' AND payment_amount BETWEEN 0 AND 100) AS e_cha
))AS a
))AS s_z
))AS xiao_zhi,
(SELECT id,sales_volume,IF(sales_volume>x_a,x_a,sales_volume) AS x_a ,IF(sales_volume<x_i,x_i,sales_volume) AS x_i  FROM (
(SELECT id,sales_volume FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活'AND category_name = '洗护清洁剂/卫生巾/纸/香薰' AND anchor = '薇娅' AND payment_amount BETWEEN 0 AND 100) AS q,
(SELECT  e.e + e_cha.E*4 x_a FROM 
((SELECT AVG(sales_volume)  e FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活'AND category_name = '洗护清洁剂/卫生巾/纸/香薰' AND anchor = '薇娅' AND payment_amount BETWEEN 0 AND 100) AS e ,
(SELECT STD(sales_volume) E FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活'AND category_name = '洗护清洁剂/卫生巾/纸/香薰' AND anchor = '薇娅' AND payment_amount BETWEEN 0 AND 100) AS e_cha
)) AS w,
(SELECT  e.e - e_cha.E*4 x_i FROM 
((SELECT AVG(sales_volume)  e FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活'AND category_name = '洗护清洁剂/卫生巾/纸/香薰' AND anchor = '薇娅' AND payment_amount BETWEEN 0 AND 100) AS e ,
(SELECT STD(sales_volume) E FROM zhubo202003_copy2 WHERE WEEK = 10 AND category = '生活'AND category_name = '洗护清洁剂/卫生巾/纸/香薰' AND anchor = '薇娅' AND payment_amount BETWEEN 0 AND 100) AS e_cha
))AS a)
)AS liang_d
)


)AS g ON g.id = f.id )
WHERE ROUND((f.xiao_z+g.liang_z)/2*100,2) > 60  ORDER   BY   v_xiao   DESC LIMIT 20




