from django.urls import path, include
from rest_framework import routers

from school.views import StudentViewSet, CourseViewSet, RegistrationViewSet


router = routers.DefaultRouter()
router.register("students", StudentViewSet, basename="student")
router.register("courses", CourseViewSet, basename="course")
router.register("registrations", RegistrationViewSet, basename="registration")


app_name = "school-api"
urlpatterns = [path("", include(router.urls))]
