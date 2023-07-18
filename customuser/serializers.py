from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from dj_rest_auth.serializers import LoginSerializer

class CustomRegisterSerializer(RegisterSerializer):
    full_name = serializers.CharField()
    is_provider = serializers.BooleanField()
    firebase_token = serializers.CharField()
    terms_conditions = serializers.BooleanField()

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()
        return {
            'username': self.validated_data.get('username', ''),
            'full_name': self.validated_data.get('full_name', ''),
            'email': self.validated_data.get('email', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'is_provider': self.validated_data.get('is_provider', ''),
            'firebase_token': self.validated_data.get('firebase_token', ''),
            'terms_conditions': self.validated_data.get('terms_conditions', ''),
        }
    
class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta(UserDetailsSerializer.Meta):
        fields = ('pk','username','email','full_name','is_provider', 'firebase_token', 'terms_conditions')
        read_only_fields = ('username','email','first_name','last_name')

class CustomLoginSerializer(LoginSerializer):
    username = None