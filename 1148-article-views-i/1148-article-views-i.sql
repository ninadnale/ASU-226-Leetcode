# Write your MySQL query statement below
SELECT DISTINCT author_id as id
FROM Views v1 
WHERE v1.viewer_id = v1.author_id
ORDER BY author_id
;