-- Active: 1763095420150@@127.0.0.1@3306@employees
-- ===========================================================
-- 1. GROUP BY 문제
-- ===========================================================

use employees;

-- ----------------------------------------------------------
-- G1. 성별별 직원 수
-- 테이블: employees.employees
-- ----------------------------------------------------------
select * from employees;
select gender, count(gender) from employees GROUP BY gender;


-- ----------------------------------------------------------
-- G2. 부서별 현재 직원 수
-- 테이블: employees.employees
-- ----------------------------------------------------------
select c.dept_name,count(*) from employees as e 
join dept_emp as d on e.emp_no = d.emp_no
join departments as c on c.dept_no = d.dept_no
group by d.dept_no;


-- ----------------------------------------------------------
-- G3.직급별 직원 수 (전체 이력 기준)
-- 테이블: employees.title
-- ----------------------------------------------------------

select title ,count(*) from titles group by title;

-- ----------------------------------------------------------
-- G4. 직급별 “현재” 직원 수
-- 테이블: employees.title
-- ----------------------------------------------------------
## to_date(퇴사 날짜)가 9999년이면 현재 남아있는 직원?
select title , count(*) from titles
where to_date > 2025-11-20
group by title;

-- ----------------------------------------------------------
-- G5.부서별 평균 급여 (현재 기준)
-- 테이블: employees.title
-- ----------------------------------------------------------
select * from dept_emp;
select c.dept_name,avg(salary) from salaries as s
join dept_emp as d on s.emp_no = d.emp_no
join departments as c on c.dept_no = d.dept_no
where s.to_date > 2025-11-20 
group by d.dept_no;


-- ----------------------------------------------------------
-- G6.입사 연도별 직원 수
-- 테이블: employees.employees
-- ----------------------------------------------------------
select hire_date, count(*) as '직원 수' from employees
group by hire_date;


-- ----------------------------------------------------------
-- G7.부서별 남녀 인원수
-- 테이블: employees.employees
-- ----------------------------------------------------------
select c.dept_name, gender,count(s.gender) from employees as s
join dept_emp as d on s.emp_no = d.emp_no
join departments as c on c.dept_no = d.dept_no
group by s.gender, d.dept_no
order by d.dept_no;



-- ----------------------------------------------------------
-- G8.부서별 평균 재직 일수
-- 테이블: employees.employees
-- ----------------------------------------------------------
## 재직일수 1) 퇴사일이 현재일자 이전 -> 퇴사일 - 입사일
##         2) 퇴사일이 현재일자 이후 -> 현재일자 - 입사일
select c.dept_name, avg(DATEDIFF( if(d.to_date > now(), now(), d.to_date), d.from_date)) as '평균 재직 일수'
from employees as e 
join dept_emp as d on e.emp_no = d.emp_no
join departments as c on c.dept_no = d.dept_no
group by d.dept_no;


-- ----------------------------------------------------------
-- G9.직급별 평균 급여 (현재 직급 + 현재 급여)
-- 테이블: employees.employees
-- ----------------------------------------------------------
select avg(s.salary) from salaries as s
join titles as t on s.emp_no = t.emp_no
where s.to_date > now() and t.to_date > now()
group by t.title;



-- ----------------------------------------------------------
-- G10.부서별 직원 수 + 전체 합계 ===> 누적 합계?
-- 테이블: employees.employees
-- ----------------------------------------------------------
select dept_name, count(*) from employees as e
join dept_emp as d on e.emp_no = d.emp_no
join departments as c on c.dept_no = d.dept_no
group by d.dept_no;