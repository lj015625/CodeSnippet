# Given a table of subscriptions, write a query to get the retention rate of each monthly cohort for each plan_id for the three months after sign-up.
#
#     Order your output by start_month, plan_id, then num_month.
#
#     If an end_date is in the same month as start_date we say the subscription was not retained in the first month.
#
#     If the end_date occurs in the month after the month of start_date, the subscription was not retained in the second month. And so on for the third.
#
#     The end_date field is NULL if the user has not canceled.
#
#     Example:
#
#     Input:
#
#     subscriptions table
#
#     Column	Type
#     user_id	INTEGER
#     start_date	DATETIME
#     end_date	DATETIME
#     plan_id	VARCHAR
#     Output:
#
#     Column	Type
#     start_month	DATETIME
#     num_month	INTEGER
#     plan_id	VARCHAR
#     retained	FLOAT

# first get number of months between end_date - start_date
WITH cte AS (
    SELECT
        *,
        CASE WHEN end_date IS NULL THEN 3 ELSE ((YEAR(end_date)*12+MONTH(end_date))-(YEAR(start_date)*12+MONTH(start_date))) END AS months_retained
    FROM subscriptions),

     # next count percentage of retrained 1 month
     cte1 AS (
         SELECT
             DATE(DATE_ADD(start_date, INTERVAL -day(start_date)+1 DAY)) AS start_month,
             1 AS 'num_month',
             plan_id,
             ROUND(sum(CASE WHEN months_retained >= 1 THEN 1 ELSE 0 END)/count(user_id), 2) AS retained
         FROM cte
         GROUP BY 1,2,3

         UNION

        # next count percentage of retrained 2 month
         SELECT
             DATE(DATE_ADD(start_date, INTERVAL -day(start_date)+1 DAY)) AS start_month,
             2 AS 'num_month',
             plan_id,
             ROUND(sum(CASE WHEN months_retained >= 2 THEN 1 ELSE 0 END)/count(user_id),2) AS retained
         FROM cte
         GROUP BY 1,2,3

         UNION

         # next count percentage of retrained 3 month
         SELECT
             DATE(DATE_ADD(start_date, INTERVAL -day(start_date)+1 DAY)) AS start_month,
             3 AS 'num_month',
             plan_id,
             ROUND(sum(CASE WHEN months_retained >=3 THEN 1 ELSE 0 END)/count(user_id), 2) AS retained
         FROM cte
         GROUP BY 1,2,3)

SELECT *
FROM cte1
ORDER BY 1,3,2