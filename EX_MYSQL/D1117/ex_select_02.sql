## ===========================================================
## 그룹화 : group by 그룹화_기준_컬럼명
##         select 절에 집계함수 사용 : max()/min()/sum()/mean()...
## ===========================================================
-- DB선택
use sakila;

## first_name열을 기준으로 정렬
select * from customer order by first_name;

## last_name 기준 정렬
select * from customer order by last_name asc;

## store_id, first_name 기준 정렬
select * from customer order by store_id, first_name;

## first_name, store_id 기준 정렬
select * from customer order by first_name, store_id;

## fist_name 오름차순 정렬
select * from customer order by first_name asc;

## first name 내림차순
select * from customer order by first_name desc;

## 내림 오름 조합
select * from customer order by store_id desc, first_name asc;

## 상위 10개 조회
select * from customer order by store_id desc, first_name asc limit 10;

## 101번째 부터 10개 조회
select * from customer order by customer_id asc limit 100, 10;

## 100개 건너뛰고 101번재 부터 10개 조회
select * from customer order by customer_id asc limit 10 offset 100;


## 4-4 

## 첫번째 글자 A시작
select * from customer where first_name like 'A%';

select * from customer where first_name like 'AA%';


select * from customer where first_name like '%A';