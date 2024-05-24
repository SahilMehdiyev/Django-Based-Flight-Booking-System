from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
from rest_framework.serializers import Serializer, ValidationError,ModelSerializer
from .models import Flight, User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


# User = get_user_model()

class LoginSerializer(TokenObtainPairSerializer):
    '''
        Kullanici girisi icin ozellestirilmis serializer
    '''
    
    def validate(self,attrs):
        #Email ve sifre ile kimlik dogrulama
        credentials = {
            'username': attrs.get('username'),
            'password': attrs.get('password'),
        } 
        
        user = self.get_user(credentials)
        # Varsayilan token bilgilerini al
        
        data = super().validate(attrs)
        
        # data['username'] = user.username
        
        return data
    
    def get_user(self,credentials):
        username = credentials.get('username')
        if username:
            try:
                return User.objects.get(username=username)
            except User.DoesNotExist:
                raise ValidationError('Invalid credentials')
        raise ValidationError('Email is required')
    


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'
        
        































 

# class TokenSerializer(Serializer):
    
#     def validate(self,attrs):
        
#         username = attrs.get('username')
#         password = attrs.get('password')
        
#         user = authenticate(username=username,password=password)
#         return user
    
    
#     def create(self, validated_data):
#         print(validated_data)
#         return None
        
        # user = validated_data['user']
        
        # # return [
        # #     self.child.create(attrs) for attrs in validated_data
        # # ]
        
        
        
        
    
        
        # refresh = RefreshToken.for_user(user)
        
        # json = {
        #     'refresh': str(refresh), 
        #     'accessToken': str(refresh.access_token)
        # }
        
        
        # return json