from django.urls import path
from .views import RoomList, BookingList

urlpatterns = [
    path('rooms/', RoomList.as_view(), name='room-list'),
    path('bookings/', BookingList.as_view(), name='booking-list'),
]