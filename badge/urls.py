
from django.urls import path
from . import views
from .views import VerifyBadge

urlpatterns = [
    path('create-badge', views.create_badge,name='create-badge'),
    # path('verify-form', views.verify_form,name='verify-form'),
    # path('verify', views.verify,name='verify'),
    path('verify', VerifyBadge.as_view(),name='verify'),
    path('edit-badge/<int:pk>', views.edit_badge,name='edit-badge'),
    path('delete-badge/<int:pk>', views.delete_badge,name='delete-badge'),
]
