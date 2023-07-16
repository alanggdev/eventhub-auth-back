from django.urls import include, path
from customuser.views import GoogleLogin
urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('register/', include('dj_rest_auth.registration.urls')),
    path('accounts/', include('allauth.urls')),
    path('google/connect/', GoogleLogin.as_view(), name='google_connect'),
]
