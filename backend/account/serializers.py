from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required = True, validators=[UniqueValidator(queryset=User.objects.all())])
    name = serializers.CharField(required = True)
    role = serializers.ChoiceField(required = False, choices=User.ROLE_CHOICES, allow_null=False)
    institution = serializers.CharField(required = False)
    password = serializers.CharField(required=True, write_only = True, validators=[validate_password])
    password2 = serializers.CharField(required=True, write_only = True)

    class Meta:
        model = User
        fields = ('email', 'name', 'role', 'institution', 'password', 'password2')
    
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
            role = validated_data['role'],
            institution=validated_data['institution']
        )
        user.set_password(validated_data['password'])
        user.save()
    
        return user