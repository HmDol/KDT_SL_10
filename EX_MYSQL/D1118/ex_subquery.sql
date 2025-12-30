-- db선택
use sakila;

## ================================================================
## 1. where절 subquery =-> 중첩 서브쿼리. 대부분의 서브쿼리 해당
## ================================================================
## 단일행 결과 : rosa와 동일한 customer_id인행 출력
select * from customer
where customer_id = (
    select customer_id 
    from customer 
    where first_name = 'ROSA'
    );

set @u_id = (select customer_id from customer where first_name = 'ROSA');

select * from customer
where customer_id = @u_id;

## [다중행 결과] ANA, ROSA와 동일한 customer_id의 고객정보 추출
select customer_id from customer
where first_name in('ROSA', 'ANA');


## [다중행 결과] ANA, ROSA의 지불 내용 정보 추출
select * from payment
where customer_id in (
    select customer_id from customer
    where first_name in('ROSA', 'ANA')
);


## [다중행 결과] action 장르 영화 리스트 추출
## 1. action 장르의 id 찾기  => catagory 테이블
## 2. action 장르에 해당하는 영화 id 추출 => film 테이블
## 3. action 장르에 해당하는 영화 정보 출력
select * from film where film_id in (
    select film_id 
    from film_category 
    where category_id = (
        select category_id from category
        where name = 'action'
    )
) ;