-- ===========================================================
-- 1. JOIN 문제 (J1 ~ J10)
-- ===========================================================

use employees;

-- ----------------------------------------------------------
-- J1. 직원의 이름과 현재 소속 부서명
-- 테이블: employees.employees, departments
-- ----------------------------------------------------------
select e.first_name, e.last_name, c.dept_name from employees as e
join dept_emp as d on e.emp_no = d.emp_no  
join departments as c on c.dept_no = d.dept_no
where d.to_date > now();


-- ----------------------------------------------------------
-- J2. 현재 부서 관리자 정보
-- 테이블: employees.employees, departments,dept_manager
-- ----------------------------------------------------------
## 정보 다 알려주면 되나요?
select * from dept_manager
join employees as e on dept_manager.emp_no = e.emp_no
join departments as d on dept_manager.dept_no = d.dept_no
where dept_manager.to_date > now();


-- ----------------------------------------------------------
-- J3. 직원의 현재 직급과 현재 급여
-- 테이블: employees.employees, titles, salaries
-- ----------------------------------------------------------
select e.emp_no, e.first_name, e.last_name, t.title '현재 직급', s.salary '현재 월급' from employees as e 
join titles as t on e.emp_no = t.emp_no
join salaries as s on e.emp_no = s.emp_no
where t.to_date > now() and s.to_date > now();


-- ----------------------------------------------------------
-- J4. 부서별 평균 급여 (60,000 이상인 부서만)
-- 테이블: employees.salaries, departments
-- ----------------------------------------------------------
select dept_name, avg(salary) from salaries as s
join dept_emp as d on s.emp_no = d.emp_no
join departments as c on c.dept_no = d.dept_no
where s.to_date > now()
group by d.dept_no
having avg(salary) >= 60000;



-- ----------------------------------------------------------
-- J5. 'Sales' 부서에 속한 현재 직원 목록
-- 테이블: employees.employees, departments
-- ----------------------------------------------------------
select e.emp_no, e.first_name, e.last_name from employees as e
join dept_emp as d on e.emp_no = d.emp_no
join departments as c on c.dept_no = d.dept_no
where c.dept_name = 'Sales' and d.to_date > now();


-- ----------------------------------------------------------
-- J6. 같은 부서에 속한 직원 
-- 테이블: employees.employees, departments
-- ----------------------------------------------------------
## 문제를 이해 못함...


-- ----------------------------------------------------------
-- J7. 관리자별 담당 부서 직원 수
-- 테이블: employees.dept_manager, employees, departments
-- ----------------------------------------------------------
select * from dept_manager;
select m.emp_no as '담당자 사원 번호',count(*)as '직원수' from dept_manager as m
join dept_emp as d on m.dept_no = d.dept_no
where m.to_date > now() and d.to_date > now()
group by m.emp_no;


-- ----------------------------------------------------------
-- J8. 직급 변경 이력이 있는 직원
-- 테이블: employees.employees, titles
-- ----------------------------------------------------------
## titles에서 같은 사원번호가 2개 이상인 직원?
select e.emp_no, e.first_name, e.last_name from employees as e
join titles as t on e.emp_no = t.emp_no
group by e.emp_no
having count(t.title) > 1;



-- ----------------------------------------------------------
-- J9. 같은 급여를 받는 직원 
-- 테이블: employees.salaries, employees
-- ----------------------------------------------------------
## 직원의 수를 보여 달라는거 맞나요?
select s.salary, count(*) as '급여가 같은 사람 수' from salaries as s
join employees as e on s.emp_no = e.emp_no
group by s.salary
having count(*) > 1;

-- ----------------------------------------------------------
-- J10. 직원별 최근 급여 이력만 조회
-- 테이블: employees.employees, salaries
-- ----------------------------------------------------------
-- select * from salaries;
select e.emp_no, e.first_name, e.last_name, s.salary from employees as e
join salaries as s on e.emp_no = s.emp_no
where s.to_date > now();
