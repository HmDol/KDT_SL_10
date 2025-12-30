-- ===========================================================
-- 1. SUBQUERY 문제(S1 ~ S10)
-- ===========================================================

use employees;

-- ----------------------------------------------------------
-- S1. 전체 평균 급여보다 많이 받는 직원
-- 테이블: employees.employees, salaries
-- ----------------------------------------------------------
-- select * from employees;
-- select * from salaries;
select emp_no, last_name, first_name from employees
where emp_no in (
    select emp_no from salaries
    where to_date > now() and salary > (
        select avg(salary) from salaries
        where to_date > now()
    )
);

-- ----------------------------------------------------------
-- S2. 'Sales' 부서에 속한 직원들
-- 테이블: employees.employees, departments
-- ----------------------------------------------------------
select * from employees as e
where emp_no in (
    select d.emp_no from dept_emp as d
    join departments as c on d.dept_no = c.dept_no
    where c.dept_name = 'Sales' and d.to_date > now()
);

-- ----------------------------------------------------------
-- S3. 급여 기록이 한 번도 없는 직원 
-- 테이블: employees.employees
-- ----------------------------------------------------------
## 급여 테이블에 사원 번호 없는 사람?
select emp_no, first_name, last_name from employees
where emp_no not in (
    select emp_no from salaries
);


-- ----------------------------------------------------------
-- S4. 부서별 평균 급여가 전체 평균보다 높은 부서
-- 테이블: employees.salaries, departments
-- ----------------------------------------------------------
-- select * from salaries;
select dept_name from departments
where dept_no in (
    select d.dept_no from departments as d 
    join dept_emp as de on d.dept_no = de.dept_no
    join salaries as s on de.emp_no = s.emp_no
    where s.to_date > now()
    group by d.dept_no
    having avg(s.salary) > (
        select avg(salary) from salaries
        where to_date > now()
    )
)


-- ----------------------------------------------------------
-- S5. 각 직원의 최대 급여와 현재 급여
-- 테이블: employees.employees, salaries
-- ----------------------------------------------------------
select s.emp_no, e.first_name, e.last_name ,max(salary), min(salary) from salaries as s
join employees as e on s.emp_no = e.emp_no
group by emp_no;


-- ----------------------------------------------------------
-- S6. 특정 직원(10001)과 같은 급여를 받는 직원들
-- 테이블: employees.employees, salaries
-- ----------------------------------------------------------\
select emp_no, first_name, last_name from employees
where emp_no in (
    select s.emp_no from salaries as s
    where s.salary = (
        select salary from salaries
        where emp_no = 10001 and to_date > now()
    ) and s.to_date > now()
);



-- ----------------------------------------------------------
-- S7. 직급이 'Manager'인 부서의 모든 직원
-- 테이블: employees.employees, titles, departments
-- ----------------------------------------------------------



-- ----------------------------------------------------------
-- S8. 직원 수가 가장 많은 부서 Top 3
-- 테이블: employees.departments
-- ----------------------------------------------------------



-- ----------------------------------------------------------
-- S9. 부서 이동 이력이 있는 직원
-- 테이블: employees.employees
-- ----------------------------------------------------------


-- ----------------------------------------------------------
-- S10. 직원 수가 가장 많은 부서에 속한 직원들
-- 테이블: employees.employees, departments
-- ----------------------------------------------------------
