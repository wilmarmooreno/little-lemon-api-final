from django.urls import path
from . import views
from .views import BookingViewSet

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),

    path('booking/', BookingViewSet.as_view({'get': 'list', 'post': 'create'})),
]