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
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.guest_name} -> {self.room.number}"

    def save(self, *args, **kwargs):
        delta = self.check_out - self.check_in
        days = delta.days

        if days <= 0:
            days = 1

        self.total_price = self.room.price * days
        super().save(*args, **kwargs)
