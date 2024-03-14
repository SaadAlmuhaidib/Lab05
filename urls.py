from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add, name='add'),
    path('', views.index, name='index'),
]

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # Include the myapp URLs
]
