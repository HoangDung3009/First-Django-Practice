from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path(r'<int:product_id>/', views.details, name='details')
]
