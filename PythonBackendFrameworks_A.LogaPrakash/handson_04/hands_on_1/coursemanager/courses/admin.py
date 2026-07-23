from django.contrib import admin
from .models import Department, Student, Course, Enrollment, Professor

# Register your models to make them visible and manageable in the Django Admin panel.

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_id', 'dept_name', 'head_of_dept', 'budget')
    search_fields = ('dept_name', 'head_of_dept')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'first_name', 'last_name', 'email', 'department', 'enrollment_year')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('department', 'enrollment_year')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'course_name', 'course_code', 'credits', 'department')
    search_fields = ('course_name', 'course_code')
    list_filter = ('department',)


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('enrollment_id', 'student', 'course', 'enrollment_date', 'grade')
    list_filter = ('grade',)


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('professor_id', 'prof_name', 'email', 'department', 'salary')
    search_fields = ('prof_name', 'email')
    list_filter = ('department',)
