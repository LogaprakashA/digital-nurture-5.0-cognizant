create table departments(
    department_id serial primary key,
    department_name varchar(50) not null,
    hod_name varchar(100) ,
    budget decimal(15,2) 
);


CREATE TABLE students(
    student_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    department_id INT REFERENCES departments(department_id),
    enrollment_date DATE
);

create table courses(
    course_id serial primary key,
    course_name varchar(100) not null,
    course_code varchar(10) unique not null,
    department_id int references departments(department_id),
    credits int not null,
    foreign key (department_id) references departments(department_id)
);

create table enrollments(
    enrollment_id serial primary key,
    student_id int references students(student_id),
    course_id int references courses(course_id),
    enrollment_date date not null,
    grade varchar(2),
    foreign key (student_id) references students(student_id),
    foreign key (course_id) references courses(course_id)
);

create table professors(
    professor_id serial primary key,
    first_name varchar(50) not null,
    last_name varchar(50) not null,
    email varchar(100) unique not null,
    department_id int references departments(department_id),
    hire_date date not null,
    salary decimal(15,2) not null,
    foreign key (department_id) references departments(department_id)
);


-- 1NF: Each table has a primary key and all columns contain atomic values. There are no repeating groups or arrays in any of the tables.
-- 2NF: All non-key attributes are fully functionally dependent on the primary key. In the students table, for example, the department_id is dependent on the student_id, and in the courses table, the department_id is dependent on the course_id.
-- 3NF: There are no transitive dependencies. In the students table, for example, 


alter table students
add column phone_number varchar(15);

alter table courses
add column max_seats int;

alter table students
drop column phone_number;


