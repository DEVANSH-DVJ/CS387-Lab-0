WITH relname
AS (
	SELECT course_id,
		COUNT(ID) AS countt
	FROM takes
	GROUP BY course_id
	)
SELECT MAX(countt)
FROM relname;
