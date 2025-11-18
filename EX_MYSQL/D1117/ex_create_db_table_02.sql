-- ======================================================
-- 실습용 DB : DoItsql
--       TB : doit_tb
-- ======================================================
-- DB 생성
CREATE DATABASE IF NOT EXISTS DoItsql;

-- DB 선택
USE DoItsql;

-- TB 생성
CREATE TABLE IF NOT EXISTS doit_tb
(
    col_1 int PRIMARY key AUTO_INCREMENT,
    col_2 varchar(50),
    col_3 int
);


CREATE TABLE IF NOT EXISTS data_tb
(
    col_2 varchar(50),
    col_3 int,
    col_4 char(2)
);

-- drop table doit_tb;
-- TB 확인
SHOW TABLES;

-- TB 구조 확인
desc doit_tb;


-- 데이터 추가 
INSERT INTO doit_tb VALUES 
(1, 'TEST1', 10),
(2, 'TEST2', 20),
(3, 'TEST3', 30),
(4, 'TEST4', 40);

INSERT INTO data_tb VALUES 
('TEST11', 10, 'T'),
('TEST22', 23, 'F'),
('TEST33', 14, 'D'),
('TEST44', 17, 'A'),
('TEST55', 67, 'C'),
('TEST66', 64, 'T'),
('TEST77', 29, 'S'),
('TEST88', 78, 'T'),
('TEST99', 98, 'D'),
('TEST00', 82, 'U');

-- auto_increment 자동 증가
insert into doit_tb (col_2, col_3) VALUES
('ok', 100);

insert into doit_tb (col_2, col_3) VALUES
('hello', 101), ('yes', 102);

## auto_increment 컬럼도 값 지정
INSERT INTO doit_tb VALUES 
(10, 'auto-increment 무시', 11);

## 다시 auto-increment 하면?
insert into doit_tb (col_2, col_3) VALUES
('다시 auto-increment 하면??', 101);



## ==================================================
## select 결과 => insert로 삽입
## data tb => doit tb로 데티ㅓ 추가
## ==================================================
insert into doit_tb(col_2, col_3)
select col_2, col_3 from data_tb;

## ==================================================
## select 결과 => create로 생성
## ==================================================
create table copytb as (
    select * from data_tb
);


## 전체 테이블 조회
select * from doit_tb;
select * from copytb;

-- AE 설정값 변경, 간격 5로 변경
SET GLOBAL AUTO_INCREMENT_increment = 5;

select LAST_INSERT_ID() '마지막 AE 번호';

