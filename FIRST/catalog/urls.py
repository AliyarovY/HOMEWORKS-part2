from django.urls import path
from django.views.decorators.cache import cache_page

from . import views


urlpatterns = [
    path('', cache_page(70)(Index.as_view()), name='catalog'),
    path('create/', views.VersionCreate.as_view(), name='create'),
]
