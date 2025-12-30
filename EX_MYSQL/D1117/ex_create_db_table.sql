-- ======================================================
-- 실습용 DB : MYDB
--       TB : User 
-- ======================================================
CREATE DATABASE IF NOT EXISTS MYDB;

USE MYDB;

CREATE TABLE IF NOT EXISTS User
(
    id int PRIMARY KEY,      
    name VARCHAR(10) NOT NULL,
    age int NOT NULL,
    hometown VARCHAR(6) NOT NULL,
    address VARCHAR(50),
    gender CHAR(1) DEFAULT '남'
);

SHOW TABLES;

-- 데이터 추가 
INSERT INTO user VALUES 
(3,  '김민아', 23, '부산', '부산시', '여'),
(4,  '이지은',  9, '대구', '부산시 동래', '여'),
(7,  '이지은', 29, '서울', '서울시', '여'),
(9,  '고길동', 20, '서울', '서울시 동래', '남'),
(12, '박나림', 37, '부산', '부산시 동래', '여'),
(13, '장지원', 25, '울산', '울산시 을주', '여');


INSERT INTO user (id, name, age, hometown, gender) VALUES 
(2,  '마징가', 14, '파주', '남'),
(5,  '박영우', 47, '파주', '남'),
(6,  '김철수', 31, '울산', '남'),
(8,  '홍길동', 51, '서울', '남'),
(10, '마테영', 49, '파주', '남'),
(11, '김진우', 44, '대구', '남'),
(14, '김동현', 31, '파주', '남'),
(15, '박지니', 60, '서울', '여'),
(16, '김덕현', 71, '대구', '남');


select * from user;