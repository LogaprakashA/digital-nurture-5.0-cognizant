from django.db import models


# ---------------- DEPARTMENT ----------------
class Department(models.Model):
    """Represents a college department."""
    department_id = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length=100)
    head_of_dept = models.CharField(max_length=100, null=True, blank=True)
    budget = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)

    class Meta:
        db_table = 'departments'

    def __str__(self):
        return self.dept_name


# ---------------- STUDENT ----------------
class Student(models.Model):
    """Represents a student enrolled in the college."""
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    enrollment_year = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'students'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# ---------------- COURSE ----------------
class Course(models.Model):
    """Represents a course offered by a department."""
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=150)
    course_code = models.CharField(max_length=20, unique=True, null=True, blank=True)
    credits = models.IntegerField(null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    duration_months = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'courses'

    def __str__(self):
        return f"{self.course_name} ({self.course_code})"


# ---------------- ENROLLMENT ----------------
class Enrollment(models.Model):
    """Tracks which student is enrolled in which course and their grade."""
    GRADE_CHOICES = [
        ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F'),
    ]
    enrollment_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField(null=True, blank=True)
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES, null=True, blank=True)

    class Meta:
        db_table = 'enrollments'

    def __str__(self):
        return f"{self.student} -> {self.course} | Grade: {self.grade}"


# ---------------- PROFESSOR ----------------
class Professor(models.Model):
    """Represents a professor teaching in a department."""
    professor_id = models.AutoField(primary_key=True)
    prof_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        db_table = 'professors'

    def __str__(self):
        return self.prof_name
