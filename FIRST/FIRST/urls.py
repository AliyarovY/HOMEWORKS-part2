from django.conf.urls.static import static
from django.contrib import admin


from FIRST import settings
from django.urls import path, include



urlpatterns = [
    path('feedbck', include('feedbck.urls')),
    path('admin/', admin.site.urls),
    path('catalog', include(('catalog.urls', 'cat'), namespace='cat')),
    path('contacts', include(('contacts.urls', 'cc'), namespace='cc')),
    path('', include('home.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

