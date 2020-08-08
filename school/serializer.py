from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from school.models import Student, Course, Registration


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = "__all__"
        validators = [
            UniqueTogetherValidator(
                queryset=Registration.objects.all(),
                fields=["student", "period"],
                message="A student can be only registered in one course per period",
            )
        ]


class StudentRegistrationsSerializer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source="course.description")
    period = serializers.SerializerMethodField()

    class Meta:
        model = Registration
        fields = ["course", "period"]

    def get_period(self, obj):
        return obj.get_period_display()


class CourseRegistrationsSerializer(serializers.ModelSerializer):
    student = serializers.ReadOnlyField(source="student.name")
    period = serializers.SerializerMethodField()

    class Meta:
        model = Registration
        fields = ["student", "period"]

    def get_period(self, obj):
        return obj.get_period_display()
