from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.BookingListView.as_view(), name='booking_list'),
    path('list/<int:id>/update/', views.BookingUpdateView.as_view(), name='booking_update'),
    path('list/<int:id>/delete/', views.BookingDeleteView.as_view(), name='booking_delete'),
    path('create/', views.BookingCreateView.as_view(), name='booking_create'),
    path('detail/<int:id>/', views.BookingDetailView.as_view(), name='booking_detail'),
]