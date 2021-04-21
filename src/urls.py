from django.contrib import admin
from django.urls import include, path
from django.views.generic import base

from rest_framework import routers

from src.apps.widgets.views import WidgetViewSet


router = routers.DefaultRouter()

router.register(r'widgets', WidgetViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls)
]
