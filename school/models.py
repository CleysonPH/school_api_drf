from django.db import models


class Student(models.Model):
    name = models.CharField("Nome", max_length=50)
    rg = models.CharField("RG", max_length=9)
    cpf = models.CharField("CPF", max_length=11)
    birth_date = models.DateField(
        "Data de Nascimento", auto_now=False, auto_now_add=False
    )

    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"

    def __str__(self):
        return self.name


class Course(models.Model):
    LEVEL_CHOICES = (("B", "Básico"), ("I", "Intermediário"), ("A", "Avançado"))

    code = models.CharField("Código", max_length=10, unique=True)
    description = models.CharField("Descrição", max_length=100)
    level = models.CharField(
        "Nível",
        max_length=1,
        choices=LEVEL_CHOICES,
        blank=False,
        null=False,
        default="B",
    )

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def __str__(self):
        return self.code


class Registration(models.Model):
    PERIOD_CHOICES = (
        ("M", "Matutino"),
        ("V", "Verpertino"),
        ("N", "Noturno"),
    )

    student = models.ForeignKey(
        "school.Student", verbose_name="Aluno", on_delete=models.CASCADE
    )
    course = models.ForeignKey(
        "school.Course", verbose_name="Curso", on_delete=models.CASCADE
    )
    period = models.CharField("Período", max_length=1, choices=PERIOD_CHOICES)

    class Meta:
        verbose_name = "Matrícula"
        verbose_name_plural = "Matrículas"

    def __str__(self):
        return f"{self.student} - {self.course}"
