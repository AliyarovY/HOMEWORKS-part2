from django.urls import path

from .views import *



urlpatterns = [
    path('registration/', Registration.as_view(), name='registration'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('verify/', VerifyPage.as_view(), name='verify'),
    path('recovery/', Recovery.as_view(), name='recovery')
]