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
