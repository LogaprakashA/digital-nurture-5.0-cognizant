"""
orm_queries.py — Hands-On 2: Django ORM Queries Demo
=====================================================
Run this script via: python manage.py shell < orm_queries.py
Or use: exec(open('orm_queries.py').read()) from inside the Django shell.

This script covers:
  Step 16: Create seed data (Departments, Courses, Students, Enrollments)
  Step 17: Filter query using FK traversal with double underscore (__)
  Step 18: Annotate query to count courses per department
  Step 19: select_related to fetch students + department in one SQL query
  Step 20: F() expression to update budgets without loading into Python
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coursemanager.settings')
django.setup()

from django.db.models import Count, F
from django.db import connection
from courses.models import Department, Course, Student, Enrollment
import datetime

print("=" * 60)
print("  Hands-On 2: Django ORM Queries")
print("=" * 60)

# ------------------------------------------------------------------
# STEP 16: CREATE SEED DATA
# ------------------------------------------------------------------
print("\n--- Step 16: Creating seed data ---")

# Clear existing data to keep script idempotent
Enrollment.objects.all().delete()
Student.objects.all().delete()
Course.objects.all().delete()
Department.objects.all().delete()

# Create 2 Departments
cs_dept = Department.objects.create(
    name='Computer Science',
    head_of_dept='Dr. Ramesh Kumar',
    budget=850000.00
)
ec_dept = Department.objects.create(
    name='Electronics',
    head_of_dept='Dr. Priya Nair',
    budget=620000.00
)
print(f"  Created departments: {cs_dept}, {ec_dept}")

# Create 4 Courses
dsa = Course.objects.create(name='Data Structures & Algorithms', code='CS101', credits=4, department=cs_dept)
dbms = Course.objects.create(name='Database Management Systems', code='CS102', credits=3, department=cs_dept)
oop = Course.objects.create(name='Object Oriented Programming', code='CS103', credits=4, department=cs_dept)
circuit = Course.objects.create(name='Circuit Theory', code='EC101', credits=3, department=ec_dept)
print(f"  Created courses: {dsa}, {dbms}, {oop}, {circuit}")

# Create 5 Students
s1 = Student.objects.create(first_name='Arjun', last_name='Mehta', email='arjun@college.edu', department=cs_dept, enrollment_year=2022)
s2 = Student.objects.create(first_name='Priya', last_name='Suresh', email='priya@college.edu', department=cs_dept, enrollment_year=2022)
s3 = Student.objects.create(first_name='Rohan', last_name='Verma', email='rohan@college.edu', department=ec_dept, enrollment_year=2021)
s4 = Student.objects.create(first_name='Sneha', last_name='Patel', email='sneha@college.edu', department=cs_dept, enrollment_year=2023)
s5 = Student.objects.create(first_name='Vikram', last_name='Das', email='vikram@college.edu', department=ec_dept, enrollment_year=2022)
print(f"  Created 5 students: {s1}, {s2}, {s3}, {s4}, {s5}")

# Create 4 Enrollments
e1 = Enrollment.objects.create(student=s1, course=dsa, enrollment_date=datetime.date(2022, 7, 1), grade='A')
e2 = Enrollment.objects.create(student=s1, course=dbms, enrollment_date=datetime.date(2022, 7, 1), grade='B')
e3 = Enrollment.objects.create(student=s2, course=dsa, enrollment_date=datetime.date(2022, 7, 1), grade='B')
e4 = Enrollment.objects.create(student=s3, course=circuit, enrollment_date=datetime.date(2021, 7, 1), grade='A')
print(f"  Created 4 enrollments")

# ------------------------------------------------------------------
# STEP 17: FILTER — courses in Computer Science using FK traversal
# ------------------------------------------------------------------
print("\n--- Step 17: Filter courses in 'Computer Science' dept ---")
# Double underscore (__) traverses the ForeignKey relationship
cs_courses = Course.objects.filter(department__name='Computer Science')
print(f"  Courses in Computer Science: {[str(c) for c in cs_courses]}")

# ------------------------------------------------------------------
# STEP 18: ANNOTATE — count number of courses per department
# ------------------------------------------------------------------
print("\n--- Step 18: Annotate — course count per department ---")
dept_course_counts = Department.objects.values('name').annotate(
    course_count=Count('courses')
)
for dept in dept_course_counts:
    print(f"  {dept['name']}: {dept['course_count']} course(s)")

# ------------------------------------------------------------------
# STEP 19: select_related — fetch students + dept in single SQL JOIN
# ------------------------------------------------------------------
print("\n--- Step 19: select_related — single JOIN query for students ---")
# Reset the query log
connection.queries_log.clear()
students = list(Student.objects.select_related('department').all())
print(f"  Fetched {len(students)} students with departments in 1 query")
for s in students:
    print(f"    {s.first_name} {s.last_name} -> Dept: {s.department.name}")
print(f"  Total DB queries used: {len(connection.queries)}")

# ------------------------------------------------------------------
# STEP 20: F() UPDATE — increase all department budgets by 10%
# ------------------------------------------------------------------
print("\n--- Step 20: F() update — increase all budgets by 10% ---")
print("  Budgets BEFORE update:")
for d in Department.objects.all():
    print(f"    {d.name}: {d.budget}")

# F() objects reference the DB column value — no Python fetch needed
rows_updated = Department.objects.update(budget=F('budget') * 1.1)
print(f"  Updated {rows_updated} department(s) using F() expression")

print("  Budgets AFTER update:")
for d in Department.objects.all():
    print(f"    {d.name}: {d.budget:.2f}")

print("\n" + "=" * 60)
print("  All ORM queries completed successfully!")
print("=" * 60)
