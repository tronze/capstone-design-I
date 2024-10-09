from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from .models import User, Teacher, Student

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required = True, validators=[UniqueValidator(queryset=User.objects.all())])
    name = serializers.CharField(required = True)
    password = serializers.CharField(required=True, write_only = True, validators=[validate_password])
    password2 = serializers.CharField(required=True, write_only = True)

    class Meta:
        model = User
        fields = ('email', 'name', 'password', 'password2')
    
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({
                "password" : "Password fields didn't match"
            })
        
        return data

    def create(self, validated_data):
        user = User.objects.create(
            email = validated_data['email'],
            name = validated_data['name'],
        )
        user.set_password(validated_data['password'])
        user.save()
    
        return user
    
class TeacherSerializer(UserSerializer):
    email = serializers.EmailField(required=True)
    subject = serializers.CharField(required=True)
    institution = serializers.CharField(required=True)

    class Meta(UserSerializer.Meta):
        model = Teacher
        fields = UserSerializer.Meta.fields + ('institution', 'subject')

    def create(self, validated_data):
        teacher = Teacher.objects.create(
            email = validated_data['email'],
            name = validated_data['name'],
            institution = validated_data['institution'],
            subject = validated_data['subject']
        )
        teacher.save()

        return teacher    

class StudentSerializer(UserSerializer):
    email = serializers.EmailField(required=True)
    school = serializers.CharField(required=True)
    grade = serializers.CharField(required=True)

    class Meta(UserSerializer.Meta):
        model = Student
        fields = UserSerializer.Meta.fields + ('school', 'grade')

    def create(self, validated_data):
        student = Student.objects.create(
            email = validated_data['email'],
            name = validated_data['name'],
            school=validated_data['school'],
            grade=validated_data['grade']
        )
        student.save()

        return student