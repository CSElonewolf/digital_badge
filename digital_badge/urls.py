
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('create-badge', views.create_badge,name='create-badge'),
]
