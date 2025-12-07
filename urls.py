from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect
from Bstudy import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Bstudy/', include(('Bstudy.urls', 'Bstudy'), namespace='Bstudy')),
    path('auth/', include(('auth_utils.urls', 'auth_utils'), namespace='auth_utils')),
    path('auth/', include('django.contrib.auth.urls')),
    path('', lambda request: redirect('Bstudy:login'), name='home_redirect'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
