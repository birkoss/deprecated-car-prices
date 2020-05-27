from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'paymentTypes', views.PaymentTypeViewSet)
router.register(r'makes', views.MakeViewSet, basename='make')

urlpatterns = [
    path('', include(router.urls)),
]
