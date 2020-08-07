from rest_framework import viewsets

from school.models import Student
from school.serializer import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """"Show all students in the database"""

    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """"Show all courses in the database"""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
