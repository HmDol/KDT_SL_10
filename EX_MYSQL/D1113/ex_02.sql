-- 	1줄 주석 기호
# 	1줄 주석 가능
/*
	여러줄 주석
*/
## ---------------------------------------------
## Test 데이터베이스에 데이터 추가
## ---------------------------------------------
## 데이터베이스 선택 : use DB이름;
use test;

## 데이터베이스에 존재하는 테이블 확인 : show tables;
show tables;

## 테이블 구조 확인 : desc 테이블이름;
desc tbl_product;

## 데이터 추가 : 모든 컬럼에 데이터 추가
## 컬럼 수와 순서 일치 필수!
## insert into 테이블이름 values (컬럼별 값...);
insert into tbl_product values (1, 'TV', 1000);
insert into tbl_product values (1, 'TV', 1000), (2,'의자', 2580);

## 데이터 추가 : 일부 컬럼에 추가
## insert into 테이블이름(컬럼명...) values (컬럼별 값...);
insert into tbl_product(pid, price) values (20, 5900);
insert into tbl_product(pid, price) values (20, 5900), (22, 51900), (21, 3900);

## => price 필드/컬럼 제약조건 : not null 즉, 빈칸을 허용하지 않음!! 반드시 데이터 입력
-- insert into tbl_product(pid, pname) values (30, 'bag');
insert into tbl_product(price) values (9999);

## 데이터 조회 : 1) 모든 컬럼 조회
## select * from 테이블이름;
select * from tbl_product;

## 데이터 조회 : 2) 일부 데이터 조회
## select 컬럼... from 테이블 이름;-- 
select pid,price from tbl_product;


select * from tbl_product;

