from rest_framework import serializers
from .models import Room, Booking

# Перекладач для кімнат
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'  # Перекласти всі поля (number, price, etc.)

# Перекладач для бронювань
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'