from django.contrib import admin

from school.models import Student


@admin.register(Student)
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "rg", "cpf", "birth_date"]
    list_display_link = ["id", "nome"]
    search_fields = ["nome"]
    list_per_page = 20
