from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from core import views

router = routers.DefaultRouter()
router.register(r'code_generated', views.CodeGeneratedViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^api/', include(router.urls)),
]