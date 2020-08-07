from django.contrib import admin

from school.models import Student, Course


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
