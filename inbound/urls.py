from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AsnListViewSet, AsnDetailViewSet

router = DefaultRouter()
router.register(r'asnlist', AsnListViewSet, basename='asnlist')
router.register(r'asndetail', AsnDetailViewSet, basename='asndetail')

urlpatterns = [
    path('', include(router.urls)),
]
