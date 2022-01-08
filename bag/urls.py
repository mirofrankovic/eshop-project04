from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name= 'view_bag'),
    path('add/<item_id>/', views.add_to_mybag, name= 'add_to_mybag'),
    path('adjust/<item_id>/', views.adjust_mybag, name= 'adjust_mybag'),
    path('remove/<item_id>/', views.remove_from_mybag, name= 'remove_from_mybag'),
]
