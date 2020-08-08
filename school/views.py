from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from school.models import Student, Course, Registration
from school.serializer import (
    StudentSerializer,
    CourseSerializer,
    RegistrationSerializer,
    StudentRegistrationsSerializer,
    CourseRegistrationsSerializer,
)


class StudentViewSet(viewsets.ModelViewSet):
    """Show all students in the database"""

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CourseViewSet(viewsets.ModelViewSet):
    """Show all courses in the database"""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class RegistrationViewSet(viewsets.ModelViewSet):
    """Show all registrations in the the database"""

    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class StudentRegistrations(generics.ListAPIView):
    """Show the registrations of a specific student"""

    serializer_class = StudentRegistrationsSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Registration.objects.filter(student_id=self.kwargs.get("pk"))


class CourseRegistrations(generics.ListAPIView):
    """Show the students of a specific course"""

    serializer_class = CourseRegistrationsSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Registration.objects.filter(course_id=self.kwargs.get("pk"))
