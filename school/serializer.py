from rest_framework import serializers

from school.models import Student, Course


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
