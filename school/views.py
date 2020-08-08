from rest_framework import viewsets, generics

from school.models import Student, Course, Registration
from school.serializer import (
    StudentSerializer,
    CourseSerializer,
    RegistrationSerializer,
    StudentRegistrationsSerializer,
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
    """Show all registrations in the the database"""

    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer


class StudentRegistrations(generics.ListAPIView):
    """Show the registrations of a specific student"""

    serializer_class = StudentRegistrationsSerializer

    def get_queryset(self):
        return Registration.objects.filter(student_id=self.kwargs.get("pk"))
