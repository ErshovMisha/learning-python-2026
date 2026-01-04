from rest_framework import serializers
from datetime import date
from .models import Room, Booking

# Перекладач для кімнат
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'  # Перекласти всі поля (number, price, etc.)

# Перекладач для бронювань
class BookingSerializer(serializers.ModelSerializer):
    # Явно кажемо: це поле сервер віддає, але не приймає від клієнта
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Booking
        fields = '__all__'

    def validate(self, data):
        check_in = data['check_in']
        check_out = data['check_out']
        if check_out <= check_in:
            raise serializers.ValidationError("Check-out date must be after check-in date.")
        if check_in < date.today():
            raise serializers.ValidationError("You cannot book a room in the past!")
        return data