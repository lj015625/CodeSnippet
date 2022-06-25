-- Write a SQL query to select the 2nd highest salary in the engineering department. If more than one person shares the highest salary, the query should select the next highest salary.
SELECT salary FROM
    (SELECT department_id,
    salary,
    RANK() OVER (partition by department_id order by salary desc) as rank_num
    FROM employees e JOIN departments d ON e.department_id = d.id
    WHERE d.name = 'engineering') sub
WHERE rank_num = 2