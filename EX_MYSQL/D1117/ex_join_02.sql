## ==================================================================
## join : 테이블 조합으로 원하는 데이터 추출 / 선택
##  - 종류 : 내부(inner) / 외부(outer)
## ==================================================================
## db 선택 및 테이블 생성
## ==================================================================
-- db선택
use sakila;

-- 데이터 조회
select * from customer; select * from address;


-- 내부 조인 : equi join : 두개 테이블에 기준 컬럼이 같이 동일한 것만 선택
--             customer tb, address tb
--             고객 정보에 상세 주소 정보 선택
select c.first_name, c.last_name, a.address
from customer as c inner join address as a
on c.address_id = a.address_id;


-- 내부 조인 : equi join : 두개 테이블에 기준 컬럼이 같이 동일한 것만 선택
--             customer tb, address tb, city tb
--             고객 정보의 도시명, 상세 주소 정보 선택
select c1.first_name, c1.last_name,c2.city, a.address
from customer as c1 inner join address as a on c1.address_id = a.address_id
inner join city as c2 on c2.city_id = a.city_id;



-- 내부조인 : none equi : 특정 컬럼의 조건이 참인 것만 선택
select *
from a inner join b
on a.id > 22;