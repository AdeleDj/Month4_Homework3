from django.urls import path
from . import views

urlpatterns = [
    path('twain/', views.TwainView.as_view(), name='twain'),
    path('remarque/', views.RemarqueView.as_view(), name='remarque'),
    path('tolstoi/', views.TolstoiView.as_view(), name='tolstoi'),
    path('', views.BookListView.as_view(), name='book_list'),
    path('book/<int:id>/', views.BookDetailView.as_view(), name='book_detail'),
]