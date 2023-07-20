from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client

from dj_rest_auth.registration.views import SocialLoginView

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist
from customuser.serializers import CustomUserDetailsSerializer
from customuser.models import CustomUser
import json

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client

def custom_response(msg, response, status):
    data ={
        "message": msg,
        "pay_load": response,
        "status": status,
    }
    res= json.dumps(data)
    response = json.loads(res)
    return response

@api_view(['GET'])
def getUserInformation(request, id, format=None):
    try:
        user = CustomUser.objects.get(pk=id)
        serializer = CustomUserDetailsSerializer(user)
        return Response(custom_response("Success", serializer.data, status=status.HTTP_200_OK))
    except ObjectDoesNotExist:
        return Response(custom_response("Error", "Not found", status=status.HTTP_404_NOT_FOUND))