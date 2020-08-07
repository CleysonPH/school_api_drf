from django.urls import path, include
from rest_framework import routers

from school.views import StudentViewSet, CourseViewSet


router = routers.DefaultRouter()
router.register("students", StudentViewSet, basename="student")
router.register("courses", CourseViewSet, basename="course")


app_name = "school-api"
urlpatterns = [path("", include(router.urls))]
