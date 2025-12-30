-- db선택
use sakila;

## ================================================================
## 1. where절 subquery =-> 중첩 서브쿼리. 대부분의 서브쿼리 해당
##    연산자 in, any, all, exists 활용
## ================================================================
#
set @u_id = (select customer_id from customer where first_name = 'ROSA');

select * from customer
where customer_id = @u_id;

## [다중행 결과] ANA, ROSA와 동일한 customer_id의 고객정보 추출
-- 연산자 in
select customer_id from customer
where first_name in('ROSA', 'ANA');


## [다중행 결과] ANA, ROSA의 지불 내용 정보 추출
select * from payment
where customer_id in (
    select customer_id from customer
    where first_name in('ROSA', 'ANA')
);

-- 연산자 any : 서브쿼리 결과 다중행 중 한개라도 True 면 True
select * from customer
where customer_id = any(
    select customer_id from customer
    where first_name in ('ROSA', 'ANA')
); 


-- 연산자 exists : 서브쿼리 결과 다중행 중 한개라도 True 면 True
## 반환되는 존재 여부만 관심. 실제 반환 데이터 관심 없음.
select * from customer
where not exists(
    select 1 from customer
    where first_name in ('ROSA', 'ANA')
); 



