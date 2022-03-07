from rest_framework import serializers
from django.contrib.auth.models import User

# User serializer
class RegisterationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only = True, style={'input_type':'password'})
    class Meta:
        model = User
        fields = ['username','email','password','password2']    #password2 is not user model field just for confimr password
        extra_kwargs = {
            'password':{'write_only':True},
            'email': {'required':True}
        }
        
    def save(self):
        password = self.validated_data.get('password')
        email = self.validated_data['email']
        password2 = self.validated_data.get('password2')
        
        if password != password2:
            raise serializers.ValidationError({"Error":"Passwords do not match"})
        
        if User.objects.filter(email = email).exists():
            raise serializers.ValidationError({"Error":"User with this Email already Exist"})
        
        account = User(
            email = email,
            username = self.validated_data['username']
        )
        account.set_password(password)
        account.save()
        
        return account
        