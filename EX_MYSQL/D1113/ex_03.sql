## ===================================
## 내장 데이터베이스 활용 - 데이터 조회
## ===================================
## DB선택 : use DB이름;
use sakila;

## table 구조 : desc /describe 테이블이름;
desc customer;

## [1] 간단한 데이터 조회 ===============================
## 고객의 first_name만 조회
select first_name from customer;
## 고객의 first_name, last_name 조회
select first_name, last_name from customer;

## [2] 조건에 맞는 데이터 조회 ===========================
## where 조건;
-- fist_name 이 'MARIA'인 고객
select first_name, customer_id, active, create_date 
from customer 
where first_name = 'MARIA';

-- customer_id 가 9인 고객 정보 4개
select first_name, customer_id, active, create_date 
from customer 
where customer_id = 9;

-- [실1] 현재 활동중인 고객 정보면 추출
select * from customer where active=1;

-- [실2] 이메일이 없는 고객
select * from customer where email is null;

-- [실2] 고객id가 짝수인 고객 정보
select * from customer where not customer_id % 2;

select * from customer;