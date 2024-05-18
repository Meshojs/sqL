create database users ;
use users ; 
SET SQL_SAFE_UPDATES = 0;
create table data (
	id int not null auto_increment , 
    name varchar(255) not null ,
    primary key(id)
);
select * from data ;
alter table 
data add age int ; 
insert into 
data(name , age) 
values("mesho" , 18) , ("ali" , 20 ) , ("mo",12);
select age 
from data where age > 15 ; 
update data 
set age = 17  
where age < 18 ;
select 
count( distinct age ) from data ; 
select sum(age) from data ;
select * from data ; 
alter table data add anotherId int ;
update data 
set anotherId = Id;