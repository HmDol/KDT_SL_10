## ==================================================================
## join : 테이블 조합으로 원하는 데이터 추출 / 선택
##  - 종류 : 내부(inner) / 외부(outer)
## ==================================================================
## db 선택 및 테이블 생성
## ==================================================================
-- db선택
use mydb;

-- tb 생성
create table a (
    id int PRIMARY KEY,
    ename char(3) not null,
    mgr char(3) not null
);

create table b (
    id int PRIMARY KEY,
    kname char(3) not null
);

-- 데이터 삽입
insert into a VALUES
(1, 'aaa' , 'top'),(2, 'bbb' , 'aaa'),(3, 'ccc' , 'bbb'),
(11, '111' , 'ccc'),(22, '222' , '111'),(33, '333' , '111');

insert into b VALUES
(1, '가'), (2,'나'), (3, '다'), (4,'라라'),( 5,'마마마'), (6, '바바바');

-- 데이터 조회
select * from a; select * from b;


-- 내부 조인 : equi join : 두개 테이블에 기준 컬럼이 같이 동일한 것만 선택
select *
from a inner join b
on a.id = b.id;


-- 내부조인 : none equi : 특정 컬럼의 조건이 참인 것만 선택
select *
from a inner join b
on a.id > 22;