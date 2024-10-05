from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required = True)
    name = serializers.CharField(required = True)
    password = serializers.CharField(required=True, write_only = True)
    password2 = serializers.CharField(required=True, write_only = True)
    
    class Meta:
        model = User
        fields = ('email', 'name', 'password', 'password2')
    
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({
                "password" : "Pass word fields didn't match"
            })
        
        return data

    def create(self, validated_data):
        user = User.objects.create(
            email = validated_data['email'],
            name = validated_data['name'],
        )
        token = RefreshToken.for_user(user)
        user.set_password(validated_data['password'])
        user.refreshtoken = token
        user.save()
    
        return user