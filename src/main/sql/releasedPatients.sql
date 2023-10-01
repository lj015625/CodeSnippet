# A hospital is studying patient flows to optimize their resource placement.
#
# Write a query to find all dates where the hospital released more patients than the day prior.
#
# Note: You may assume that the table has no missing dates.
#
# Input:
#
# released_patients table
#
# Column	        Type
# release_date	    DATE
# released_patients	INTEGER
# Output:
#
# Column	        Type
# release_date	    DATE
# released_patients	INTEGER

SELECT
       r1.release_date
     , r1.released_patients
FROM released_patients r1
LEFT JOIN released_patients r2 ON r1.release_date = r2.release_date + 1
WHERE r1.released_patients > r2.released_patients;


SELECT *,
       LAG(released_patients, 1) OVER (ORDER BY release_date) AS prev_released_patients
FROM released_patients