from user_app.models import CustomUser
from rest_framework import serializers

class RegistrationSerializer(serializers.ModelSerializer):
        password2 = serializers.CharField(style= {'input_type':'password'},write_only=True)

        class Meta:
                model = CustomUser
                fields = ['username', 'password', 'password2', 'email']
                extra_kwargs = {
                        'password': {'write_only': True}
                }

        def save(self):

                password = self.validated_data['password']
                password2 = self.validated_data['password2']

                if password != password2:
                        raise serializers.ValidationError({'error': 'Password mismatch'})

                if CustomUser.objects.filter(email=self.validated_data['email']).exists():
                        raise serializers.ValidationError({'error': 'Email already exists'})

                account = CustomUser(email=self.validated_data['email'], username=self.validated_data['username'])
                account.set_password(password)
                account.save()
                return account