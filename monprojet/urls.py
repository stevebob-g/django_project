from django.contrib import admin
from django.urls import path
from car_shop.views import liste_vehicules, detail_vehicule
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', liste_vehicules, name='catalogue'),
    path('vehicule/<int:id>/', detail_vehicule, name='detail_vehicule'),
]

# Indispensable pour afficher les photos en développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)