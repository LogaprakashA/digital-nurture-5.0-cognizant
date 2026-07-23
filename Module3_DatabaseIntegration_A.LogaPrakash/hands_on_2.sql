insert into departments (department_name, hod_name, budget) values
('Computer Science', 'Dr. Smith', 500000.00),
('Mathematics', 'Dr. Johnson', 300000.00),
('Physics', 'Dr. Lee', 400000.00);

insert into students (first_name, last_name, email, department_id, enrollment_date) values
('Alice', 'Brown', 'alice.brown@example.com', 1, '2023-09-01'),
('Bob', 'Smith', 'bob.smith@example.com', 2, '2023-09-01'),
('Charlie', 'Davis', 'charlie.davis@example.com', 3, '2023-09-01');

insert into courses (course_name, course_code, department_id, credits) values
('Introduction to Computer Science', 'CS101', 1, 3),
('Calculus I', 'MATH101', 2, 4),
('General Physics', 'PHYS101', 3, 4);

insert into enrollments (student_id, course_id, enrollment_date, grade) values
(1, 1, '2023-09-01', 'A'),
(2, 2, '2023-09-01', 'B'),
(3, 3, '2023-09-01', 'A');

insert into professors (first_name, last_name, email, department_id, hire_date, salary) values
('Dr. Smith', 'Smith', 'dr.smith@example.com', 1, '2020-01-15', 75000.00),
('Dr. Johnson', 'Johnson', 'dr.johnson@example.com', 2, '2019-08-20', 70000.00),
('Dr. Lee', 'Lee', 'dr.lee@example.com', 3, '2018-12-10', 72000.00);

update students
set first_name = 'Murugan'
where student_id = 1;

update courses
set course_name = 'Advanced Computer Science'
where course_id = 1;

select * from students
where first_name = 'Murugan';


select * from students;
select * from courses;
select * from enrollments;

select * from professors;
where salary between 70000 and 75000;

select * from students
where email like '%@example.com';

select extract(year from enrollment_date) as enrollment_year, count(*) as student_count
from students
group by extract(year from enrollment_date);
order by enrollment_year;



select s.first_name, s.lastname as full_name, d.department_name
from students s
join departments d on s.department_id = d.department_id;

select s.student_id, s.first_name, s.last_name
from students s
left join enrollments e on s.student_id = e.student_id
where e.enrollment_id is null;

SELECT 
    c.course_name,
    COUNT(e.student_id) AS total_students
FROM courses c
LEFT JOIN enrollments e
    ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name
ORDER BY c.course_name;