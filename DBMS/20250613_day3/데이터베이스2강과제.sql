-- CREATE DATABASE refund_corp;
-- USE refund_corp;
-- employees 테이블을 생성해주세요
CREATE TABLE employees (
 	 id INT PRIMARY KEY AUTO_INCREMENT,
     name VARCHAR(100),
     positon VARCHAR(100),
     salary DECIMAL(10,2)
 );
-- 직원 데이터를 employees에 추가하세요 
INSERT INTO employees (name, positon, salary) VALUE ('혜린', 'PM', 90000);
INSERT INTO employees (name, positon, salary) VALUE ('은우', 'Frontend', 80000);
INSERT INTO employees (name, positon, salary) VALUE ('가을', 'Backend', 92000);
INSERT INTO employees (name, positon, salary) VALUE ('지수', 'Frontend', 78000);        
INSERT INTO employees (name, positon, salary) VALUE ('민혁', 'Frontend', 96000);
INSERT INTO employees (name, positon, salary) VALUE ('하온', 'Backend', 130000);


ALTER TABLE employees RENAME COLUMN positon TO position;

-- 모든 직원의 이름과 연봉 정보만을 조회하는 쿼리를 작성해주세요
SELECT name,salary FROM employees;

-- Frontend 직책을 가진 직원 중에서 연봉이 90000 이하인 직원의 이름과 연봉을 조회하세요
SELECT * FROM employees
WHERE position = 'Frontend' AND salary <= 90000; 

-- PM 직책을 가진 모든 직원의 연봉을 10% 인상한 후 그 결과를 확인하세요.
UPDATE employees SET salary = salary * 1.1 WHERE position = 'PM';
SELECT * FROM employees;
SELECT * FROM employees WHERE position = 'PM';

-- 모든 Backend 직책을 가진 직원의 연봉을 5% 인상하세요
UPDATE employees SET salary = salary * 1.05 WHERE position = 'Backend';

-- 민혁 사원의 데이터를 삭제하세요
DELETE FROM employees WHERE name = '민혁';

-- 모든 직원을 position 별로 그룹화하여 각 직책의 평균 연봉을 계산하세요.
SELECT position, AVG(salary) AS average_salary FROM employees GROUP BY position;

-- employees 테이블을 삭제하세요.
DELETE FROM employees;
DROP TABLE employees;