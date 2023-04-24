from rest_framework import serializers
from academy_app.models import School, Teacher, Student, Course, Section, Chapter

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ["id", "name"]

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ["id", "user", "school"]

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "user", "school"]

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "name", "school", "teacher"]

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ["id", "title", "course"]

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ["id", "title", "content", "section"]