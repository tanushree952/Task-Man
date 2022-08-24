from django.contrib import admin
from django.urls import path , include
from rest_framework import routers, serializers, viewsets
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('App.urls')),
    path('api-auth/', include('rest_framework.urls')),

]
