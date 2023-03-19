from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from stock.views import ProductViewSet, SaleViewSet

router = routers.DefaultRouter()

#API
router.register(r'sales', SaleViewSet, basename='sales_details')
router.register(r'product', ProductViewSet, basename='user_details')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls), name='api'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]