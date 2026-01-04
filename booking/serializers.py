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
    class Meta:
        model = Booking
        fields = '__all__'

    # Ця функція запускається автоматично, коли хтось надсилає дані
    def validate(self, data):
        check_in = data['check_in']
        check_out = data['check_out']

        # Перевірка 1: Дата виїзду має бути пізніше дати заїзду
        if check_out <= check_in:
            raise serializers.ValidationError("Check-out date must be after check-in date.")

        # Перевірка 2: Не можна бронювати в минулому
        if check_in < date.today():
            raise serializers.ValidationError("You cannot book a room in the past!")

        return data