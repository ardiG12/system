from django.contrib import admin
from django.urls import path,include
from core import views
from core.views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
