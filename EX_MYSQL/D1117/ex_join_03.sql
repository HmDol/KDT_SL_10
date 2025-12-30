## ==================================================================
## join : 테이블 조합으로 원하는 데이터 추출 / 선택
##  - 종류 : 내부(inner) / 외부(outer)
## ==================================================================
## db 선택 및 테이블 생성
## ==================================================================
-- db선택
use sakila;

-- 데이터 조회
select * from store; select * from customer;


-- 외부 조인 : equi join : 두개 테이블에 기준 컬럼이 같이 동일한 것만 선택
--             address tb, store tb
--             주소와 관련된 상점 정보 추출
select c.first_name , s.last_update
from customer as c left outer join store as s
on c.store_id = s.store_id;

-- 내부 조인 : equi join : 두개 테이블에 기준 컬럼이 같이 동일한 것만 선택
--             customer tb, address tb, city tb
--             고객 정보의 도시명, 상세 주소 정보 선택
select c1.first_name, c1.last_name,c2.city, a.address
from customer as c1 inner join address as a on c1.address_id = a.address_id
inner join city as c2 on c2.city_id = a.city_id;

## left outer join : 왼쪽 테이블 모두 선택 => 오른쪽 테이블에 없으면 null
select a.address , s.store_id
from address as a left join store as s 
on a.address_id = s.address_id;


## right outer join :오른쪽 테이블 모두 선택 => 왼쪽 테이블에 없으면 null
select a.address , s.store_id
from address as a right join store as s 
on a.address_id = s.address_id; 



## full outer join : left + right outer join , mysql 지원X
select a.address , s.store_id
from address as a left join store as s 
on a.address_id = s.address_id

union

select a.address , s.store_id
from address as a right join store as s 
on a.address_id = s.address_id; 


## full outer join : left + right outer join + 교집합 제외
select a.address , s.store_id
from address as a left join store as s 
on a.address_id = s.address_id
where s.address_id is null

union

select a.address , s.store_id
from address as a right join store as s 
on a.address_id = s.address_id
where a.address_id is null;
