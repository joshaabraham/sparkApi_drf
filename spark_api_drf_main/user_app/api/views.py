from rest_framework.decorators import api_view
from rest_framework.response import Response
from user_app.api.serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token

# Create your views here.

@api_view(['POST'])
def regitration_view(request): 

        if request.method == 'POST':
                serializer = RegistrationSerializer(data=request.data)

                data = {}

                if serializer.is_valid():
                        account = serializer.save()
                        
                        data['response'] = 'registration successfull.'
                        data['username'] = account.username
                        data['email']= account.email

                        token = Token.objects.get(user=account).key
                        data['token'] = token  

                else:
                        data = serializer.errors
                        
                return Response(data)

