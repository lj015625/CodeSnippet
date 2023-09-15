# Given the employees and departments table, write a query to get the top 3 highest employee salaries by department.
# If the department contains less that 3 employees, the top 2 or the top 1 highest salaries should be listed
# (assume that each department has at least 1 employee).

WITH employee_ranks AS(
    SELECT
        department_id,
        first_name,
        last_name,
        salary,
        RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS ranks
    FROM employees

)

SELECT
    CONCAT(er.first_name,' ', er.last_name) AS employee_name,
    d.name AS department_name,
    salary
FROM employee_ranks er
         LEFT JOIN departments d ON d.id = er.department_id
WHERE ranks < 4
ORDER BY department_name ASC, salary DESC