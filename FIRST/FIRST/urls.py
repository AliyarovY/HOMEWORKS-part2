from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('feedbck', include('feedbck.urls')),
    path('admin/', admin.site.urls),
    path('catalog', include('catalog.urls')),
    path('', include('home.urls'))
]
