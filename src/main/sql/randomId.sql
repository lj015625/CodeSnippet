# Let’s say we have a table with an id and name fields. The table holds over 100 million rows
# and we want to sample a random row in the table without throttling the database.
#
# Write a query to randomly sample a row from this table.
#
# Input:
#
# big_table table
#
# Columns	Type
# id	    INTEGER
# name	    VARCHAR

SELECT r1.id, r1.name
FROM big_table AS r1
INNER JOIN (
    SELECT CEIL(RAND() * (SELECT MAX(id) FROM big_table) # RAND() returns a decimal between (0,1) then multiply max id
               ) AS id
) AS r2
ON r1.id >= r2.id
ORDER BY r1.id ASC
LIMIT 1