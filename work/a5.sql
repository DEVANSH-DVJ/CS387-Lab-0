SELECT ID
FROM takes
WHERE course_id = 'CS-101'
	AND ID IN (
		SELECT ID
		FROM TAKES
		WHERE course_id = 'CS-190'
		);
