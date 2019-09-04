from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('myApp.urls')),
    path('accounts/',include('accounts.urls')),
    path('realtors/', include('realtors.urls')),
    path('contacts/',include('contacts.urls')),
    #for social authentication
    path('oauth/', include('social_django.urls'), name='social'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
