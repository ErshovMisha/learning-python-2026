from rest_framework import generics, filters  # <--- Додали filters
from django_filters.rest_framework import DjangoFilterBackend  # <--- Додали це
from .models import Room, Booking
from .serializers import RoomSerializer, BookingSerializer


class RoomList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    # Підключаємо можливості фільтрації та сортування
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]

    # 1. Фільтри (точне співпадіння)
    # Можна писати ?capacity=2 або ?price=150
    filterset_fields = ['capacity', 'price']

    # 2. Сортування
    # Можна писати ?ordering=price (спочатку дешеві) або ?ordering=-price (спочатку дорогі)
    ordering_fields = ['price', 'capacity']

    # 3. Пошук (текстовий)
    # Можна писати ?search=101
    search_fields = ['number']


class BookingList(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    # Для бронювань фільтри поки не додаємо, щоб не ускладнювати