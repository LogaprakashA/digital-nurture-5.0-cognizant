from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, DECIMAL, Boolean, Time
from sqlalchemy.orm import declarative_base, relationship

engine = create_engine(
    "mysql+mysqlconnector://root:DhAnRaJ%40%23123@localhost/college_db",
    echo=True
)

Base = declarative_base()

# ---------------- DEPARTMENTS ----------------
class Department(Base):
    __tablename__ = "departments"

    department_id = Column(Integer, primary_key=True, autoincrement=True)
    department_name = Column(String(100), nullable=False)
    head_of_dept = Column(String(100))
    budget = Column(DECIMAL(12,2))

    students = relationship("Student", back_populates="department")
    courses = relationship("Course", back_populates="department")
    professors = relationship("Professor", back_populates="department")


# ---------------- STUDENTS ----------------
class Student(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    date_of_birth = Column(Date)
    department_id = Column(Integer, ForeignKey("departments.department_id"))
    enrollment_year = Column(Integer)
    is_active = Column(Boolean, default=True, server_default='1')

    department = relationship("Department", back_populates="students")
    enrollments = relationship("Enrollment", back_populates="student")


# ---------------- COURSES ----------------
class Course(Base):
    __tablename__ = "courses"

    course_id = Column(Integer, primary_key=True, autoincrement=True)
    course_name = Column(String(150), nullable=False)
    course_code = Column(String(20), unique=True)
    credits = Column(Integer)
    department_id = Column(Integer, ForeignKey("departments.department_id"))
    duration_months = Column(Integer)

    department = relationship("Department", back_populates="courses")
    enrollments = relationship("Enrollment", back_populates="course")
    schedules = relationship("CourseSchedule", back_populates="course")


# ---------------- ENROLLMENTS ----------------
class Enrollment(Base):
    __tablename__ = "enrollments"

    enrollment_id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey("students.student_id"))
    course_id = Column(Integer, ForeignKey("courses.course_id"))
    enrollment_date = Column(Date)
    grade = Column(String(2))

    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")


# ---------------- PROFESSORS ----------------
class Professor(Base):
    __tablename__ = "professors"

    professor_id = Column(Integer, primary_key=True, autoincrement=True)
    prof_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)
    department_id = Column(Integer, ForeignKey("departments.department_id"))
    salary = Column(DECIMAL(10,2))

    department = relationship("Department", back_populates="professors")


# ---------------- COURSE SCHEDULES ----------------
class CourseSchedule(Base):
    __tablename__ = "course_schedules"

    schedule_id = Column(Integer, primary_key=True, autoincrement=True)
    course_id = Column(Integer, ForeignKey("courses.course_id"), nullable=False)
    day_of_week = Column(String(20), nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)

    course = relationship("Course", back_populates="schedules")


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("All ORM Models Created Successfully")