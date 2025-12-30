use sakila;

-- = 연산자로 특정 값 조회
SELECT * FROM customer WHERE first_name = 'MARIA';

-- address_id가 200
SELECT * FROM customer WHERE address_id = 200;

-- address_id가 200 미만
SELECT * FROM customer WHERE address_id < 200;

-- first_name이 MARIA
SELECT * FROM customer WHERE first_name = 'MARIA';

-- first_name이 MARIA 미만
SELECT * FROM customer WHERE first_name < 'MARIA';

-- 특정 날짜
SELECT * FROM payment WHERE payment_date = '2005-07-09 13:24:07';

-- 특정날짜 미만 미만인 행을 조회
SELECT * FROM payment WHERE payment_date < '2005-07-09';

-- 정해진 범위에 해당하는 데이터 조회
SELECT * FROM customer WHERE address_id BETWEEN 5 AND 10;

-- 범위 날짜 포함한 날짜 조회
SELECT * FROM payment WHERE payment_date BETWEEN '2005-06-17' AND '2005-07-19';

-- 정확한 날짜를 조회
SELECT * FROM payment WHERE payment_date = '2005-07-08 07:33:56';

-- first_name M~O 범위
SELECT * FROM customer WHERE first_name BETWEEN 'M' AND 'O';

-- first_name M~O 범위의 값을 제외
SELECT * FROM customer WHERE first_name NOT BETWEEN 'M' AND 'O';

-- 두 조건을 만족
SELECT * FROM city WHERE city = 'Sunnyvale' AND country_id= 103;

-- 두 개의 비교 연산식을 만족
SELECT * FROM payment WHERE payment_date >= '2005-06-01' AND payment_date <= '2005-07-05';

-- 한 조건을 만족한 경우
SELECT * FROM customer WHERE first_name = 'MARIA' OR first_name = 'LINDA';

-- OR를 두 개 이상
SELECT * FROM customer WHERE first_name = 'MARIA' OR first_name = 'LINDA' OR first_name = 'NANCY';

-- IN을 활용
SELECT * FROM customer WHERE first_name IN ('MARIA', 'LINDA','NANCY');

-- 요구 사항을 반영
SELECT * FROM city WHERE country_id = 103 OR country_id = 86 AND city IN ('Cheju', 'Sunnyvale', 'Dallas');

-- 순서를 변경
SELECT * FROM city WHERE country_id = 86 OR country_id = 103 AND city IN ('Cheju', 'Sunnyvale', 'Dallas' );

-- 소괄호로 우선순위
SELECT * FROM city WHERE (country_id = 103 OR country_id = 86) AND city IN ('Cheju', 'Sunnyvale', 'Dallas');

-- IN, AND
SELECT * FROM city WHERE country_id IN (103, 86) AND city IN ('Cheju', 'Sunnyvale', 'Dallas' );

-- Null이 있는 테이블
SELECT * FROM address;

-- = 연산자를 사용해 NULL 데이터 조회
SELECT * FROM address WHERE address2 = NULL;

-- address2 열에서 NULL인 데이터 조회
SELECT * FROM address WHERE address2 IS NULL;

-- address2 열에서 NULL이 아닌 데이터 조회
SELECT * FROM address WHERE address2 IS NOT NULL;

-- address2 열에서 NULL이 아닌 데이터 조회
SELECT * FROM address WHERE address2 = '';