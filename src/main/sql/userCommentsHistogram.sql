# Write a SQL query to create a histogram of the number of comments per user in the month of January 2020.
# Note: Assume bin buckets class intervals of one.
# Note: Comments that were created outside of January 2020 should be counted in a “0” bucket

with user_comment_count as (
    SELECT
        u.id,
        count(c.created_at) comment_count
    from users u
             left join comments c
                       on u.id = c.user_id
                           and c.created_at
                              BETWEEN '2020-01-01' AND '2020-01-31'
    group by u.id
)

select comment_count, count(id) as frequency
from user_comment_count
group by comment_count