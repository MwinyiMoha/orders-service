from django.urls import path
from rest_framework import routers

from orders.views import OrderViewSet
from products.views import ProductViewSet

router = routers.DefaultRouter()
router.register("products", ProductViewSet)
router.register("orders", OrderViewSet)

urlpatterns = []

urlpatterns += router.urls
