from django.contrib import admin
from django.urls import include, path

from cars.api.urls import urlpatterns as cars_urlpatterns

urlpatterns = [
    path('api/', include(cars_urlpatterns)),
    path('admin/', admin.site.urls),
]
