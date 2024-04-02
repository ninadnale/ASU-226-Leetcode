# Write your MySQL query statement below
SELECT contest_id, ROUND(COUNT(user_id)/(SELECT COUNT(user_id) FROM Users)*100, 2) as percentage 
FROM Register r 
-- Users u RIGHT JOIN Register r 
-- On u.user_id = r.user_id 
GROUP BY contest_id 
ORDER BY percentage DESC, contest_id ASC
;