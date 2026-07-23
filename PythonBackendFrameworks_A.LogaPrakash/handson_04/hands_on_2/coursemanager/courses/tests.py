from django.test import TestCase
from django.db import IntegrityError
from django.db.models import Count, F
from .models import Department, Course, Student, Enrollment
import datetime


# ------------------------------------------------------------------
# DEPARTMENT TESTS
# ------------------------------------------------------------------
class DepartmentModelTest(TestCase):

    def setUp(self):
        self.dept = Department.objects.create(
            name='Computer Science',
            head_of_dept='Dr. Ramesh Kumar',
            budget=850000.00
        )

    def test_str_returns_name(self):
        """__str__ should return the department name."""
        self.assertEqual(str(self.dept), 'Computer Science')

    def test_fields_saved_correctly(self):
        """All department fields should be saved accurately."""
        d = Department.objects.get(pk=self.dept.pk)
        self.assertEqual(d.head_of_dept, 'Dr. Ramesh Kumar')
        self.assertAlmostEqual(float(d.budget), 850000.00)


# ------------------------------------------------------------------
# COURSE TESTS
# ------------------------------------------------------------------
class CourseModelTest(TestCase):

    def setUp(self):
        self.dept = Department.objects.create(name='Computer Science')
        self.course = Course.objects.create(
            name='Data Structures & Algorithms',
            code='CS101',
            credits=4,
            department=self.dept
        )

    def test_str_returns_name(self):
        """__str__ should return the course name."""
        self.assertEqual(str(self.course), 'Data Structures & Algorithms')

    def test_code_is_unique(self):
        """Course codes must be unique — duplicate should raise IntegrityError."""
        with self.assertRaises(Exception):
            Course.objects.create(name='Another Course', code='CS101', credits=3, department=self.dept)

    def test_course_fk_to_department(self):
        """Course should be linked to the correct department."""
        self.assertEqual(self.course.department.name, 'Computer Science')

    def test_cascade_delete(self):
        """Deleting a department should delete its courses (CASCADE)."""
        dept_id = self.dept.pk
        self.dept.delete()
        self.assertFalse(Course.objects.filter(department_id=dept_id).exists())


# ------------------------------------------------------------------
# STUDENT TESTS
# ------------------------------------------------------------------
class StudentModelTest(TestCase):

    def setUp(self):
        self.dept = Department.objects.create(name='Electronics')
        self.student = Student.objects.create(
            first_name='Arjun',
            last_name='Mehta',
            email='arjun@college.edu',
            department=self.dept,
            enrollment_year=2022
        )

    def test_str_returns_full_name(self):
        """__str__ should return first + last name."""
        self.assertEqual(str(self.student), 'Arjun Mehta')

    def test_email_is_unique(self):
        """Student emails must be unique."""
        with self.assertRaises(Exception):
            Student.objects.create(
                first_name='Other',
                last_name='Student',
                email='arjun@college.edu'
            )

    def test_student_fk_to_department(self):
        """Student should be linked to the correct department."""
        self.assertEqual(self.student.department.name, 'Electronics')


# ------------------------------------------------------------------
# ENROLLMENT TESTS
# ------------------------------------------------------------------
class EnrollmentModelTest(TestCase):

    def setUp(self):
        self.dept = Department.objects.create(name='Computer Science')
        self.course = Course.objects.create(name='DBMS', code='CS102', credits=3, department=self.dept)
        self.student = Student.objects.create(
            first_name='Priya', last_name='Suresh',
            email='priya@college.edu', department=self.dept
        )
        self.enrollment = Enrollment.objects.create(
            student=self.student,
            course=self.course,
            enrollment_date=datetime.date(2022, 7, 1),
            grade='A'
        )

    def test_str_contains_student_and_course(self):
        """__str__ should mention student and course."""
        self.assertIn('Priya Suresh', str(self.enrollment))
        self.assertIn('DBMS', str(self.enrollment))

    def test_unique_together_prevents_duplicate_enrollment(self):
        """Enrolling same student in same course twice should raise an error."""
        with self.assertRaises(Exception):
            Enrollment.objects.create(
                student=self.student,
                course=self.course,
                enrollment_date=datetime.date(2022, 8, 1),
                grade='B'
            )

    def test_grade_is_nullable(self):
        """Grade field should allow null."""
        dept2 = Department.objects.create(name='Mech')
        course2 = Course.objects.create(name='Thermo', code='ME101', credits=3, department=dept2)
        enroll = Enrollment.objects.create(
            student=self.student,
            course=course2,
            enrollment_date=datetime.date(2023, 7, 1)
        )
        self.assertIsNone(enroll.grade)


# ------------------------------------------------------------------
# ORM QUERY TESTS
# ------------------------------------------------------------------
class ORMQueryTest(TestCase):

    def setUp(self):
        self.cs = Department.objects.create(name='Computer Science', budget=850000)
        self.ec = Department.objects.create(name='Electronics', budget=620000)
        self.c1 = Course.objects.create(name='DSA', code='CS101', credits=4, department=self.cs)
        self.c2 = Course.objects.create(name='DBMS', code='CS102', credits=3, department=self.cs)
        self.c3 = Course.objects.create(name='Circuit Theory', code='EC101', credits=3, department=self.ec)
        self.s1 = Student.objects.create(first_name='Arjun', last_name='Mehta', email='arjun@c.edu', department=self.cs)

    def test_filter_by_department_name(self):
        """Filter courses by dept name using FK traversal (double underscore)."""
        cs_courses = Course.objects.filter(department__name='Computer Science')
        self.assertEqual(cs_courses.count(), 2)

    def test_annotate_course_count_per_department(self):
        """Annotate departments with their course count."""
        result = Department.objects.values('name').annotate(
            course_count=Count('courses')
        ).order_by('name')
        cs_row = next(r for r in result if r['name'] == 'Computer Science')
        self.assertEqual(cs_row['course_count'], 2)

    def test_select_related_single_query(self):
        """select_related should fetch students with their department in one query."""
        students = list(Student.objects.select_related('department').all())
        # Access department name without extra query
        for s in students:
            _ = s.department.name  # Would cause extra query without select_related

    def test_f_expression_budget_update(self):
        """F() update should increase budgets by 10% without fetching to Python."""
        Department.objects.update(budget=F('budget') * 1.1)
        self.cs.refresh_from_db()
        self.assertAlmostEqual(float(self.cs.budget), 850000 * 1.1, places=1)
