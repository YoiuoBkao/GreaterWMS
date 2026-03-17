from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/goods/', include('goods.urls')),
    path('api/supplier/', include('supplier.urls')),
    path('api/customer/', include('customer.urls')),
    path('api/stock/', include('stock.urls')),
    path('api/inbound/', include('inbound.urls')),
    path('api/outbound/', include('outbound.urls')),
    path('api/staff/', include('staff.urls')),
]
