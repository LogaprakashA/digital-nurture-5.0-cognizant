from django.contrib import admin
from .models import Department, Course, Student, Enrollment


# ---------------- DEPARTMENT ADMIN ----------------
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'head_of_dept', 'budget']
    search_fields = ['name', 'head_of_dept']


# ---------------- COURSE ADMIN ----------------
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    # Step 23: Show multiple columns in list view
    list_display = ['name', 'code', 'credits', 'department']
    # Step 23: Enable search by name and code
    search_fields = ['name', 'code']
    # Step 24: Enable sidebar filtering by department
    list_filter = ['department']


# ---------------- STUDENT ADMIN ----------------
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'department', 'enrollment_year']
    search_fields = ['first_name', 'last_name', 'email']
    list_filter = ['department', 'enrollment_year']


# ---------------- ENROLLMENT ADMIN ----------------
@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'enrollment_date', 'grade']
    list_filter = ['grade', 'course']
    search_fields = ['student__first_name', 'student__last_name', 'course__name']
