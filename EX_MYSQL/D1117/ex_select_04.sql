## ------------------------------------------------------------------------
## 그룹화 : group by 그룹화_기준_컬럼명
##          select 절에 집계함수 사용
## -----------------------------------------------------------------------0

## db선택
use mydb;

## ------------------------------------------------------------------------
## group by 컬럼명
## ------------------------------------------------------------------------
select * from user;

select count(DISTINCT hometown) from user;


select hometown, count(*) from user group by hometown;

select hometown, count(hometown) 
from user 
group by hometown 
order by count(hometown) desc;


## ----------------------------------------------
## group by 컬럼1, 컬럼2 ...
## ----------------------------------------------
select hometown, gender
from user
group by hometown, gender
order by hometown;

select name, count(*) 
from user 
group by name;


select hometown, gender, count(*) '인원수'
from user
group by hometown, gender
order by hometown;

--- hometwon, gender 그룹화 후 성별이 남자인 그룹 데이터
select hometown, gender, count(*) '인원수'
from user
group by hometown, gender
having gender = '남'
order by hometown;
