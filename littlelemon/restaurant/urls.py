from django.urls import path, include
from . import views
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'', views.BookingView, basename='booking')

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('menuitems/', views.menuitems, name='menuitems'),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),
    path('book/', views.book, name='book'),
    path('reservations/', views.reservations, name='reservations'),
    path('menu/', views.MenuView.as_view()),
    path('menu/<int:pk>', views.SingleMenuView.as_view()),
    path('booking/', views.BookingView.as_view(), name="booking"),
]
