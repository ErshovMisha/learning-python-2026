from rest_framework import generics
from .models import Room, Booking
from .serializers import RoomSerializer, BookingSerializer

# ListCreateAPIView — це магія DRF.
# Він сам вміє робити дві речі:
# 1. GET: Показати список
# 2. POST: Створити новий запис
class RoomList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class BookingList(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer