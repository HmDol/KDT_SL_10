-- test 데이터 베이스 삭제
drop database if exists TEST;

-- Test 데이터베이스 생성
create database if not exists TEST;

-- 사용 데이터베이스 선택
use TEST;

-- 테이블 생성
create table tbl_product(
pid int,
pname varchar(10),
price int not null
);

-- 데이터 추가
insert into tbl_product value(1,'ABC', 1000);
insert into tbl_product(pid, price) values (2.3 , 1000);
-- insert into tbl_product(pid, pname) value(1,'TV');  오류남, price 없음 
insert into tbl_product values (11, 'data11', 1111) ,(22, 'data22', 2222) , (33, 'data33', 3333); 

-- 데이터 조회
select * from tbl_product