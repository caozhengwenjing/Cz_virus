select * from[dbo].[Drinks];
select * from[dbo].[Expense];
select * from[dbo].[Singer];
select * from[dbo].[Song];
select * from[dbo].[Type];
--多表连接原则有共同的字段DrinksID
--select * from 表A
--inner join 表B
--on a.字段=b.字段
select a.DrinksName,b.ExpenseDate from Drinks a
inner join Expense b
on a.DrinksID=b.DrinksID;

--select * from 表A,表B,表C,表D
--where A.字段=B.字段
--and B.字段=C.字段
--and C.字段=D.字段
select a.DrinksName,b.ExpenseDate from Drinks a,Expense b
where a.DrinksID=b.DrinksID;


--三表连接  用inner join on 放法
select * from [Type] a
inner join Song b
on a.TypeID=b.TypeID
inner join Singer c
on c.SingerID=b.SingerID

--
select * from [Type]a,Song b,Singer c
where a.TypeID=b.TypeID 
and b.SingerID=c.SingerID;

