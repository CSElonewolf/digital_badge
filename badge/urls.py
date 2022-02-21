
from django.urls import path
from . import views
urlpatterns = [
    path('create-badge', views.create_badge,name='create-badge'),
    path('verify-form', views.verify_form,name='verify-form'),
    path('verify', views.verify,name='verify'),
]
