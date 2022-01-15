SELECT ID,
	name,
	instructor.dept_name,
	building
FROM instructor,
	department
WHERE instructor.dept_name = department.dept_name;
