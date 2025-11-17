## =============================================
## Table 연동 연산 실습
## =============================================
## DB 선택 : use DB_NAME ;
use sakila;

## Table 정보 확인 : desc/describe Table_Name;
desc customer;

## [실습1] customer 테이블
## address_id가 2자리수인 고객 정보 추출
select * from customer where length(address_id) = 2;

## [실습2] customer 테이블
## 이름이 'C' ~ 'D'로 시작하는 고객 정보만 추출
select * from customer where first_name like 'C%';

## [실습3] customer 테이블
## Cheju, Dallas 고객 정보만 추출
select * from city where city in ('Cheju', 'Dallas');

## [실습4] customer 테이블
## Cheju, Dallas 고객 정보만 추출


## [실습5] customer 테이블
## 성은 A로 시작하고 이름은 E로 끝나는 고객 정보만 추출
select * from customer where first_name like 'A%' and last_name like '%E';


## [실습6] city 테이블
## 국가코드가 101인 도시들 출력
select * from city where country_id=101;

## [실습7] city 테이블
## 국가코드가 101이 도시들 중 도시명에 사이에 h가 있는 도시
select * from city where country_id = 101 and city like '%h%';

## [실습8] address 테이블 
## address2가 입려되지 않는 주소 정보만 출력
select * from address where address2 is null;


## [실습9] address 테이블 
## address2와 phone이 입려되지 않는 주소 정보만 출력
select * from address where address2 is null and phone is null;


## [실습10] payment 테이블
## 결제일이 7월인 데이터만 추출
select * from payment where payment_date like '%-07-%';
	