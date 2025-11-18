## ------------------------------------------------------------------------
## 그룹화 : group by 그룹화_기준_컬럼명
##          select 절에 집계함수 사용
## -----------------------------------------------------------------------0

## db선택
use sakila;

-- tb선택 & 상새 설명 : desc/describe tb_name
desc film;


## -----------------------------------------------------------------------
## groupby 컬럼명 1, 컬럼명 2
## -----------------------------------------------------------------------
-- special features 값 종류
select count(distinct special_features) from film;

-- special features 로 그룹화
select special_features, count(special_features) from film
group by special_features;


## ==================================================================
## group by 컬럼1, 컬럼2, ... : 여러 컬럼 기준으로 그룹화
## ==================================================================
select distinct rating from film;

## 다중 그룹화
select special_features, rating from film
group by special_features, rating;

## 각 그룹별 개수
select special_features, rating, count(rating) from film
group by special_features, rating;

## ---------------------------------------------------------------------
## count() 집계함수와 정렬 order by
## ---------------------------------------------------------------------
## special_features 로 중복 제거 후 개수 파악
select special_features, count(special_features )
from film
group by special_features


## 정렬
select special_features, count(special_features ) 'cnt'
from film
group by special_features
order by cnt;

## ====================================================================
## Having 조건 : 그룹화 후 그룹들에 대한 필터링
## ====================================================================
-- special features로 그룹;화 후 그룹이 행수가 70개 이상인 그룹만 선택 

select special_features, count(*) as 'cnt' from film
group by special_features
having count(*) >= 70;