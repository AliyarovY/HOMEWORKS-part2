from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='catalog'),
    path('create/', views.VersionCreate.as_view(), name='create'),
]
