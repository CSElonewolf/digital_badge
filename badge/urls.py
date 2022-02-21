
from django.urls import path
from . import views
urlpatterns = [
    path('create-badge', views.create_badge,name='create-badge'),
]
