from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tables', views.BookingView, basename='tables')

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuView.as_view()),
    path('menu/<int:pk>', views.SingleMenuView.as_view()),
    path('', include(router.urls)),
]
