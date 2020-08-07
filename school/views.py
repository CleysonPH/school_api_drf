from rest_framework import viewsets

from school.models import Student, Course, Registration
from school.serializer import (
    StudentSerializer,
    CourseSerializer,
    RegistrationSerializer,
)


class StudentViewSet(viewsets.ModelViewSet):
    """Show all students in the database"""

    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """Show all courses in the database"""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class RegistrationViewSet(viewsets.ModelViewSet):
    """Shwl all registrations in the the database"""

    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
