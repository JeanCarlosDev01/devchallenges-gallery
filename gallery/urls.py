from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from gallery.views import index

urlpatterns = [
    path('', index, name='gallery'),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
