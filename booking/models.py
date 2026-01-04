from django.db import models

class Room(models.Model):
    number = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField(default=1)

    def __str__(self):
        return f"Room {self.number} ({self.capacity} ppl)"

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings')
    guest_name = models.CharField(max_length=100)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f"{self.guest_name} -> {self.room.number}"
