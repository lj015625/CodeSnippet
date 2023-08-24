-- Write a query to identify customers who placed more than three transactions each in both 2019 and 2020.

SELECT
    u.name customer_name
FROM transactions t
LEFT JOIN users u ON t.user_id = u.id
GROUP BY t.user_id
HAVING
    SUM(CASE WHEN YEAR(created_at) = 2019 THEN 1 ELSE 0 END) >= 3 AND
    SUM(CASE WHEN YEAR(created_at) = 2020 THEN 1 ELSE 0 END) >= 3