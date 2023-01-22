from django.urls import path
from .views import *


urlpatterns = [

    path('', Index.as_view(), name='main'),
    path('create/', Create.as_view(), name='create'),
    path('public/', PublicOnly.as_view(), name='public'),
    path('<slug:slug>/read/', Read, name='read'),
    path('<slug:slug>/delete/', Delete.as_view(), name='delete'),
    path('<slug:slug>/update/', Update.as_view(), name='update'),

]
