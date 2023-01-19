from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tables', views.BookingView, basename='tables')

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('menuitems/', views.menuitems, name='menuitems'),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),
    path('book', views.book, name='book'),
    path('reservations', views.reservations, name='reservations'),
    path('menu/', views.MenuView.as_view()),
    path('menu/<int:pk>', views.SingleMenuView.as_view()),
    path('booking/', include(router.urls)),
    path('bookings', views.bookings, name='bookings'),
]
