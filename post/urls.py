from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register(r'', PostViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
]