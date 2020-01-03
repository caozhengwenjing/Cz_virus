##当月总额
SELECT SUM(字段) 
FROM 表名 
WHERE DATE_FORMAT( 时间字段, '%Y%m' ) = DATE_FORMAT( CURDATE( ) , '%Y%m' )

##上月
SELECT SUM(字段) 
FROM 表名 
WHERE DATE_FORMAT(时间字段, '%Y %m') = DATE_FORMAT(DATE_SUB(CURDATE(), INTERVAL 1 MONTH),'%Y %m')


##年总额
SELECT SUM(字段) 
FROM 表名 
WHERE  YEAR(时间字段)=YEAR(NOW()) 


##去年总额
SELECT SUM(字段) 
FROM 表名 
WHERE  YEAR(时间字段)=YEAR(DATE_SUB(NOW(),INTERVAL 1 YEAR))


//当年每月数据
SELECT DATE_FORMAT(TIME, "%Y-%m")AS MONTH,SUM(money)AS totalmoney 
FROM xc_capital_success
WHERE DATE_FORMAT(TIME, "%Y-%m-%d") >= "2020-01-01" AND TYPE = "薪酬代发"
GROUP BY DATE_FORMAT(TIME, "%Y-%m")


//当月每日数据
SELECT DATE_FORMAT(TIME, "%m-%d") AS MONTH,SUM(money) AS totalmoney 
FROM xc_capital_success
WHERE DATE_FORMAT(TIME, "%Y-%m-%d") >= "2019-01-01" AND DATE_FORMAT( TIME, '%Y%m' ) = DATE_FORMAT( CURDATE( ) , '%Y%m' ) AND TYPE = "薪酬代发"
GROUP BY DATE_FORMAT(TIME, "%Y-%m-%d")


//上月每天数据
SELECT DATE_FORMAT(TIME, "%m-%d") AS MONTH,SUM(money) AS totalmoney 
FROM xc_capital_success
WHERE DATE_FORMAT(TIME, '%Y %m') = DATE_FORMAT(DATE_SUB(CURDATE(), INTERVAL 1 MONTH),'%Y %m') AND TYPE = "薪酬代发"
GROUP BY DATE_FORMAT(TIME, "%Y-%m-%d")







//薪资小于一万的个数
SELECT COUNT(*),submit_time FROM xc_order_draft WHERE amount < 10000 AND order_state = 2 AND DATE_FORMAT( submit_time, '%Y%m' ) = DATE_FORMAT( CURDATE( ) , '%Y%m' )


//薪资在一万到三万之间的个数
SELECT COUNT(*),submit_time FROM xc_order_draft WHERE amount BETWEEN 10000 AND 30000 AND order_state = 2 AND DATE_FORMAT( submit_time, '%Y%m' ) = DATE_FORMAT( CURDATE( ) , '%Y%m' )


//薪资在三万到十万之间的个数
SELECT COUNT(*),submit_time FROM xc_order_draft WHERE amount BETWEEN 30000 AND 100000 AND order_state = 2 AND DATE_FORMAT( submit_time, '%Y%m' ) = DATE_FORMAT( CURDATE( ) , '%Y%m' )


//薪资在十万以上的个数
SELECT submit_time, COUNT(*) FROM xc_order_draft WHERE amount > 100000 AND order_state = 2 AND DATE_FORMAT( submit_time, '%Y%m' ) = DATE_FORMAT( CURDATE( ) , '%Y%m' )


//薪资范围汇总
SELECT mina,maxa,maxx, maxxx FROM (
(SELECT submit_time, COUNT(*)  mina FROM xc_order WHERE amount < 10000 AND order_state = 4 AND DATE_FORMAT( submit_time, '%Y%m' ) = DATE_FORMAT( CURDATE( ) , '%Y%m' )) AS mina ,
(SELECT submit_time, COUNT(*) maxa FROM xc_order WHERE amount BETWEEN 10000 AND 30000 AND order_state = 4 AND DATE_FORMAT( submit_time, '%Y%m' ) = DATE_FORMAT( CURDATE( ) , '%Y%m' )) AS  maxa,
(SELECT submit_time, COUNT(*) maxx FROM xc_order WHERE amount BETWEEN 30000 AND 100000 AND order_state = 4 AND DATE_FORMAT( submit_time, '%Y%m' ) = DATE_FORMAT( CURDATE( ) , '%Y%m' )) AS  maxx,
(SELECT  submit_time, COUNT(*) maxxx FROM xc_order WHERE amount > 100000 AND order_state = 4 AND DATE_FORMAT( submit_time, '%Y%m' ) = DATE_FORMAT( CURDATE( ) , '%Y%m' ) ) AS maxxx
)


SELECT mina,maxa,maxx, maxxx FROM (
(SELECT COUNT(*)  mina FROM xc_capital_success WHERE money < 10000 AND TYPE = "薪酬代发" AND DATE_FORMAT( TIME, '%Y%m' ) = DATE_FORMAT( CURDATE( ) , '%Y%m' )) AS mina ,
(SELECT COUNT(*) maxa FROM xc_capital_success WHERE money BETWEEN 10000 AND 30000 AND TYPE = "薪酬代发" AND DATE_FORMAT( TIME, '%Y%m' ) = DATE_FORMAT( CURDATE( ) , '%Y%m' )) AS  maxa,
(SELECT COUNT(*) maxx FROM xc_capital_success WHERE money BETWEEN 30000 AND 100000 AND TYPE = "薪酬代发"AND DATE_FORMAT( TIME, '%Y%m' ) = DATE_FORMAT( CURDATE( ) , '%Y%m' )) AS  maxx,
(SELECT COUNT(*) maxxx FROM xc_capital_success WHERE money > 100000 AND TYPE = "薪酬代发" AND DATE_FORMAT( TIME, '%Y%m' ) = DATE_FORMAT( CURDATE( ) , '%Y%m' ) ) AS maxxx
)


SELECT COUNT(*)  mina FROM xc_capital_success WHERE money < 10000 AND TYPE = "薪酬代发" AND  DATE_FORMAT(TIME, '%Y %m') = DATE_FORMAT(DATE_SUB(CURDATE(), INTERVAL 1 MONTH),'%Y %m'))

//上月
SELECT mina,maxa,maxx, maxxx FROM (
(SELECT COUNT(*)  mina FROM xc_capital_success WHERE money < 10000 AND TYPE = "薪酬代发" AND  DATE_FORMAT(TIME, '%Y %m') = DATE_FORMAT(DATE_SUB(CURDATE(), INTERVAL 1 MONTH),'%Y %m')) AS mina ,
(SELECT COUNT(*) maxa FROM xc_capital_success WHERE money BETWEEN 10000 AND 30000 AND TYPE = "薪酬代发" AND  DATE_FORMAT(TIME, '%Y %m') = DATE_FORMAT(DATE_SUB(CURDATE(), INTERVAL 1 MONTH),'%Y %m')) AS  maxa,
(SELECT COUNT(*) maxx FROM xc_capital_success WHERE money BETWEEN 30000 AND 100000 AND TYPE = "薪酬代发"AND  DATE_FORMAT(TIME, '%Y %m') = DATE_FORMAT(DATE_SUB(CURDATE(), INTERVAL 1 MONTH),'%Y %m')) AS  maxx,
(SELECT COUNT(*) maxxx FROM xc_capital_success WHERE money > 100000 AND TYPE = "薪酬代发" AND  DATE_FORMAT(TIME, '%Y %m') = DATE_FORMAT(DATE_SUB(CURDATE(), INTERVAL 1 MONTH),'%Y %m')) AS maxxx
)

//落地公司日报




 
//实施发薪数据（时间、企业、落地、金额）(前十)
SELECT submit_time,company_name,wr_company_name,amount 
FROM xc_order
WHERE DATE_FORMAT( submit_time, '%Y%m' ) = DATE_FORMAT( CURDATE( ) , '%Y%m' ) AND order_state = 4
ORDER BY submit_time DESC LIMIT 50


//上月实施发薪
SELECT submit_time,company_name,wr_company_name,amount 
FROM xc_order_draft
WHERE order_state = 2 AND DATE_FORMAT(submit_time, '%Y %m') = DATE_FORMAT(DATE_SUB(CURDATE(), INTERVAL 1 MONTH),'%Y %m')
ORDER BY submit_time DESC LIMIT 50

SELECT submit_time,company_name,wr_company_name,SUM(amount) 
FROM xc_order
WHERE order_state = 3 AND DATE_FORMAT(submit_time, '%Y %m') = DATE_FORMAT(DATE_SUB(CURDATE(), INTERVAL 1 MONTH),'%Y %m') 
GROUP BY company_name



SELECT SUM(money),company_name 
FROM xc_capital_success 
WHERE  DATE_FORMAT(TIME, '%Y %m') = DATE_FORMAT(DATE_SUB(CURDATE(), INTERVAL 1 MONTH),'%Y %m') AND TYPE = "薪酬代发" 
GROUP BY company_name


//企业对应渠道商
SELECT xc_company.company_name,xc_agent.`agent_nick` 
FROM xc_company LEFT JOIN xc_agent ON xc_company.agent_id = xc_agent.`agent_id`




//落地公司笔数金额（时间、落地、金额）
SELECT submit_time,wr_company_name,amount FROM xc_order_draft WHERE DATE_FORMAT( submit_time, '%Y%m' ) = DATE_FORMAT( CURDATE( ) , '%Y%m' ) AND order_state = 2


//当天数据总额
SELECT SUM(amount),submit_time FROM xc_order_draft WHERE TO_DAYS(submit_time) = TO_DAYS(NOW())AND order_state = 2


//近30天的数据
SELECT amount,submit_time,id FROM xc_order_draft WHERE DATE_SUB(CURDATE(), INTERVAL 14 DAY) <= DATE(submit_time)AND order_state = 2


//某年某月的数据
SELECT amount,submit_time,id FROM xc_order_draft   WHERE DATE_FORMAT(submit_time,'%Y-%m')='2019-10' AND order_state = 2


//当前这周的数据
SELECT amount,submit_time,id FROM xc_order_draft WHERE YEARWEEK(DATE_FORMAT(submit_time,'%Y-%m-%d')) = YEARWEEK(NOW())  AND order_state = 2


//上周的数据
SELECT amount,submit_time,id FROM xc_order_draft WHERE YEARWEEK(DATE_FORMAT(submit_time,'%Y-%m-%d')) = YEARWEEK(NOW())-1 AND order_state = 2


//查询当前月份或任意某个月的数据()
SELECT amount,submit_time,id FROM xc_order_draft WHERE DATE_FORMAT(submit_time,'%Y-%m')=DATE_FORMAT(NOW(),'%Y-%m') //=后面可换为具体时间，查询任意月份的数据


//查询距离当前时间6个月的数据
SELECT amount,submit_time,id FROM xc_order_draft WHERE submit_time BETWEEN DATE_SUB(NOW(),INTERVAL 6 MONTH) AND NOW();


//当月电签人数
SELECT COUNT(*) FROM xc_contract WHERE contract_status = '待签署' AND DATE_FORMAT( contract_time, '%Y%m' ) = DATE_FORMAT( CURDATE( ) , '%Y%m' )


//上月充值额度
SELECT	SUM(money) FROM xc_recharge WHERE STATUS = 2 AND  DATE_FORMAT(finish_time, '%Y %m') = DATE_FORMAT(DATE_SUB(CURDATE(), INTERVAL 1 MONTH),'%Y %m')


//上月服务费额度
SELECT	SUM(service_fee) FROM xc_recharge WHERE STATUS = 2 AND  DATE_FORMAT(finish_time, '%Y %m') = DATE_FORMAT(DATE_SUB(CURDATE(), INTERVAL 1 MONTH),'%Y %m')


//上月落地额度
SELECT COUNT(*) FROM xc_order_draft WHERE DATE_FORMAT(submit_time, '%Y %m') = DATE_FORMAT(DATE_SUB(CURDATE(), INTERVAL 1 MONTH),'%Y %m') AND order_state = 2 


SELECT  * FROM xc_order LEFT JOIN xc_salary ON xc_order.order_id = xc_salary.order_id LIMIT 10 


//明细报表
SELECT finish_time ,xc_salary.order_id,company_name,wr_company_name, payee_name,receiving_account, salary,request_time,serial_number,trade_status, xc_salary.remark 
FROM xc_order LEFT JOIN xc_salary ON xc_order.order_id = xc_salary.order_id 
LIMIT 10 


//用户报表
SELECT payee_name,xc_personnel.identity,phone,company_name,landing_company_name,identity_upload_status,sign_status,COUNT(*),SUM(salary) 
FROM xc_personnel LEFT JOIN xc_salary ON xc_personnel.name = xc_salary.payee_name  
GROUP BY xc_personnel.identity 


//落地公司明细
SELECT xc_order.submit_time,xc_order.company_name,xc_order.wr_company_name,xc_order.amount,xc_recharge.amount,xc_order.submit_time 
FROM xc_order LEFT JOIN xc_recharge ON xc_order.wr_company_id = xc_recharge.wr_company_id 
GROUP BY xc_order.wr_company_name


//落地公司日报



//企业发薪
SELECT xc_order.submit_time,xc_order.order_id,xc_order.company_name,xc_order.wr_company_name,SUM(amount),COUNT(*),xc_order.service_fee,xc_order.amount 
FROM xc_order LEFT JOIN xc_sign_sms_send_record ON xc_order.company_id = xc_sign_sms_send_record.company_id
GROUP BY xc_order.company_name


//落地公司概况
SELECT xc_order.submit_time,xc_order.wr_company_name,COUNT(*),SUM(amount) 
FROM xc_order LEFT JOIN xc_salary ON xc_order.`order_id` = xc_salary.`order_id`  
GROUP BY xc_order.wr_company_name



//落地公司概况
SELECT totaldata.a,totaldata.b,totaldata.c ,totaldata.d ,okdata.e,okde.q FROM 
(SELECT  xc_order.submit_time AS a,xc_order.wr_company_name AS b,COUNT(*) AS c,SUM(amount) AS d FROM xc_order LEFT JOIN xc_salary ON xc_order.`order_id` = xc_salary.`order_id` GROUP BY xc_order.wr_company_name ) AS totaldata,
(SELECT xc_wanrong_money.`money` AS e ,xc_wanrong_money.`wr_company_name` AS f FROM xc_wanrong_money LEFT JOIN xc_order ON  xc_order.`wr_company_id`=xc_wanrong_money.`wr_company_id`  GROUP BY xc_wanrong_money.wr_company_name )AS okdata,
(SELECT xc_recharge.amount AS q,xc_recharge.`wr_company_name` FROM xc_recharge LEFT JOIN xc_order ON xc_order.`wr_company_id`=xc_recharge.`wr_company_id` GROUP BY xc_recharge.wr_company_name ) AS okde
GROUP BY totaldata.b



//落地公司概况(用)
SELECT  xc_order.submit_time,xc_order.wr_company_name,COUNT(*),COUNT(xc_salary.id),SUM(xc_order.amount),xc_wanrong_money.`money`,xc_recharge.`money`,xc_recharge.amount, SUM(xc_salary.payee_name)
FROM xc_order ,xc_salary,xc_wanrong_money ,xc_recharge 
WHERE xc_order.`order_id` = xc_salary.`order_id`  AND   xc_order.`wr_company_id`=xc_wanrong_money.`wr_company_id` AND   xc_order.`wr_company_id`=xc_recharge.`wr_company_id` 
GROUP BY xc_order.wr_company_id


SELECT wr_company_name,money,amount FROM xc_recharge GROUP BY wr_company_name


SELECT payee_name,COUNT(xc_salary.id),xc_order.`wr_company_name` FROM xc_salary LEFT JOIN xc_order ON  xc_salary.order_id =xc_order.`order_id` GROUP BY xc_salary.`payee_name` AND xc_order.`wr_company_name`



SELECT payee_name,COUNT(xc_salary.id),xc_order.`wr_company_name`
FROM xc_salary,xc_order
WHERE xc_salary.order_id =xc_order.`order_id`
GROUP BY xc_salary.`payee_name`
LIMIT 50000





SELECT DATE_FORMAT(TIME, "%Y-%m")AS MONTH,SUM(money)AS totalmoney 
FROM xc_capital_success
WHERE YEAR(TIME)=YEAR(DATE_SUB(NOW(),INTERVAL 1 YEAR)) AND TYPE = "薪酬代发"
GROUP BY DATE_FORMAT(TIME, "%Y-%m")
















