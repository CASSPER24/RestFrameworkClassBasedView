from rest_framework import serializers, viewsets
from school.models import Student, Teacher
from django.contrib.auth.models import User

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        extra_kwargs = {'url': {'view_name': 'StudentDetail'}}




class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    students = serializers.HyperlinkedIdentityField(view_name='StudentDetail', format='html')
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'students', 'owner']
        extra_kwargs = {'url': {'view_name': 'UserDetail'}}





