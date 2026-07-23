from django.db import models


# ---------------- DEPARTMENT ----------------
class Department(models.Model):
    """Represents a college department."""
    name = models.CharField(max_length=100)
    head_of_dept = models.CharField(max_length=100, null=True, blank=True)
    budget = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


# ---------------- COURSE ----------------
class Course(models.Model):
    """Represents a course offered by a department."""
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=20, unique=True)
    credits = models.IntegerField(default=3)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name='courses'
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


# ---------------- STUDENT ----------------
class Student(models.Model):
    """Represents a student enrolled in the college."""
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, null=True, blank=True, related_name='students'
    )
    enrollment_year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['last_name', 'first_name']


# ---------------- ENROLLMENT ----------------
class Enrollment(models.Model):
    """Tracks student enrollment in a course."""
    GRADE_CHOICES = [
        ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F'),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrollment_date = models.DateField(null=True, blank=True)
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES, null=True, blank=True)

    def __str__(self):
        return f"{self.student} -> {self.course} | Grade: {self.grade or 'N/A'}"

    class Meta:
        unique_together = [['student', 'course']]
        ordering = ['enrollment_date']
