from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.booking_list, name='booking_list'),
    path('list/<int:id>/update/', views.booking_update, name='booking_update'),
    path('list/<int:id>/delete/', views.booking_delete, name='booking_delete'),
    path('create/', views.booking_create, name='booking_create'),
    path('detail/<int:id>/', views.booking_detail, name='booking_detail'),
]

urlpatterns = [
    path('', views.booking_list, name='booking_list'),
    path('<int:id>/update/', views.booking_update, name='booking_update'),
    path('<int:id>/delete/', views.booking_delete, name='booking_delete'),
    path('create/', views.booking_create, name='booking_create'),
    path('<int:id>/', views.booking_detail, name='booking_detail'),
]