SELECT course_id,
	COUNT(DISTINCT ID)
FROM takes
GROUP BY course_id;
