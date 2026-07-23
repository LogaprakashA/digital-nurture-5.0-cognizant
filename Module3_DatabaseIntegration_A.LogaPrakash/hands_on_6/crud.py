"""
TASK 3 

Comparison Before and After joinedload()

Before joinedload():
- SQLAlchemy executed multiple SQL queries.
- One query fetched Enrollment records.
- Additional queries fetched Student and Course data.
- This is called the N+1 Query Problem.
- Performance is slower because many database calls are made.

After joinedload():
- SQLAlchemy loads Enrollment, Student and Course together.
- A single JOIN query is executed.
- Database calls are reduced.
- Performance is improved.
- The N+1 Query Problem is eliminated.
"""
from sqlalchemy.orm import sessionmaker, joinedload
from hands_on_6.models import engine, Department, Student, Course, Enrollment

Session = sessionmaker(bind=engine)
session = Session()

print("\n========== STEP 80 : Database Connection ==========")
print("Database Connected Successfully")


# ===================== STEP 81 =====================
print("\n========== STEP 81 : Departments ==========")

departments = session.query(Department).all()

for dept in departments:
    print(
        dept.department_id,
        dept.department_name,
        dept.head_of_dept,
        dept.budget
    )


# ===================== STEP 82 =====================
print("\n========== STEP 82 : Students ==========")

students = session.query(Student).all()

for student in students:
    print(
        student.student_id,
        student.first_name,
        student.last_name,
        student.email,
        student.enrollment_year
    )


# ===================== STEP 83 =====================
print("\n========== STEP 83 : Students in Computer Science ==========")

cs_students = (
    session.query(Student)
    .join(Department)
    .filter(Department.department_name == "Computer Science")
    .all()
)

for student in cs_students:
    print(student.first_name, student.last_name)


# ===================== STEP 84 =====================
print("\n========== STEP 84 : Student Enrollments ==========")

enrollments = (
    session.query(Enrollment)
    .options(
        joinedload(Enrollment.student),
        joinedload(Enrollment.course)
    )
    .all()
)

for e in enrollments:
    print(
        e.student.first_name,
        "->",
        e.course.course_name,
        "| Grade:",
        e.grade
    )


# ===================== STEP 85 =====================
print("\n========== STEP 85 : Update Student ==========")

student = (
    session.query(Student)
    .filter(Student.email == "arjun.mehta@college.edu")
    .first()
)

if student:
    student.enrollment_year = 2025
    session.commit()
    print("Student Updated Successfully")
else:
    print("Student Not Found")


# ===================== STEP 86 =====================
print("\n========== STEP 86 : Delete Enrollment ==========")

enrollment = (
    session.query(Enrollment)
    .filter(Enrollment.enrollment_id == 12)
    .first()
)

if enrollment:
    session.delete(enrollment)
    session.commit()
    print("Enrollment Deleted Successfully")
else:
    print("Enrollment Not Found")


# ===================== STEP 87–91 =====================
print("\n========== STEP 87-91 : joinedload() Demo ==========")

students = (
    session.query(Student)
    .options(
        joinedload(Student.department),
        joinedload(Student.enrollments)
    )
    .all()
)

for student in students:
    print(
        student.first_name,
        "-",
        student.department.department_name,
        "- Total Enrollments:",
        len(student.enrollments)
    )

session.close()

print("\nHands-On 6 Completed Successfully")