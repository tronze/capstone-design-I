from rest_framework import serializers
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