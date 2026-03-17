from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DnListViewSet, DnDetailViewSet

router = DefaultRouter()
router.register(r'dnlist', DnListViewSet, basename='dnlist')
router.register(r'dndetail', DnDetailViewSet, basename='dndetail')

urlpatterns = [
    path('', include(router.urls)),
]
