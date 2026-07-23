from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Course, Student, Enrollment
from .serializers import (
    CourseSerializer,
    StudentSerializer,
    EnrollmentSerializer,
)


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True, methods=['get'])
    def students(self, request, pk=None):
        enrollments = Enrollment.objects.filter(course_id=pk)
        students = Student.objects.filter(
            student_id__in=enrollments.values_list('student_id', flat=True)
        )
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer