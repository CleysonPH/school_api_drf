from django.contrib import admin

from school.models import Student, Course, Registration


@admin.register(Student)
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "rg", "cpf", "birth_date"]
    list_display_links = ["id", "name"]
    search_fields = ["name"]
    list_per_page = 20


@admin.register(Course)
class CourseModelAdmin(admin.ModelAdmin):
    list_display = ["id", "code", "description"]
    list_display_links = ["id", "code"]
    search_fields = ["code"]


@admin.register(Registration)
class RegistrationModelAdmin(admin.ModelAdmin):
    list_display = ["id", "student", "course", "period"]
    list_display_links = ["id"]

