from rest_framework import serializers
from school.models import Student, Teacher
from django.contrib.auth.models import User

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'



class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    students = serializers.PrimaryKeyRelatedField(many=True, queryset=Student.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'students', 'owner']


