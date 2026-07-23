from django.test import TestCase, Client
from django.urls import reverse
from .models import Department, Student, Course, Enrollment, Professor


class HelloViewTest(TestCase):
    """Tests for the hello_view endpoint."""

    def setUp(self):
        self.client = Client()

    def test_hello_view_status_200(self):
        """GET /api/hello/ should return HTTP 200."""
        response = self.client.get('/api/hello/')
        self.assertEqual(response.status_code, 200)

    def test_hello_view_response_content(self):
        """GET /api/hello/ should return the correct message."""
        response = self.client.get('/api/hello/')
        self.assertEqual(response.content.decode(), "Course Management API is running")


class DepartmentModelTest(TestCase):
    """Tests for the Department model."""

    def setUp(self):
        self.dept = Department.objects.create(
            dept_name='Computer Science',
            head_of_dept='Dr. Ramesh Kumar',
            budget=850000.00
        )

    def test_department_str(self):
        """Department __str__ should return dept_name."""
        self.assertEqual(str(self.dept), 'Computer Science')

    def test_department_fields(self):
        """Department fields should be saved correctly."""
        self.assertEqual(self.dept.head_of_dept, 'Dr. Ramesh Kumar')
        self.assertEqual(float(self.dept.budget), 850000.00)


class StudentModelTest(TestCase):
    """Tests for the Student model."""

    def setUp(self):
        self.dept = Department.objects.create(dept_name='Electronics')
        self.student = Student.objects.create(
            first_name='Arjun',
            last_name='Mehta',
            email='arjun.mehta@college.edu',
            department=self.dept,
            enrollment_year=2022
        )

    def test_student_str(self):
        """Student __str__ should return full name."""
        self.assertEqual(str(self.student), 'Arjun Mehta')

    def test_student_department_link(self):
        """Student should be linked to the correct department."""
        self.assertEqual(self.student.department.dept_name, 'Electronics')


class CourseModelTest(TestCase):
    """Tests for the Course model."""

    def setUp(self):
        self.dept = Department.objects.create(dept_name='Mechanical')
        self.course = Course.objects.create(
            course_name='Thermodynamics',
            course_code='ME101',
            credits=3,
            department=self.dept
        )

    def test_course_str(self):
        """Course __str__ should return name and code."""
        self.assertEqual(str(self.course), 'Thermodynamics (ME101)')
