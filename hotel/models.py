from django.db import models
from django.conf import settings #user model from settings
# Create your models here.
class Room(models.Model):
    Room_Categories=(
        ('YAC', 'AC'),
        ('NAC', 'NON-AC'),
        ('DEL', 'DELUXE'),
        ('KIN', 'KING'),
        ('QUE', 'QUEEN'),
    ) #left for database,Right to show
    
    number=models.IntegerField()
    category=models.CharField(max_length=3, choices=Room_Categories)
    beds=models.IntegerField()
    capacity=models.IntegerField()

    def __str__(self): #whenever you do something with your model it will show you this representation
        return f'{self.number}.{self.category} with {self.beds} beds for {self.capacity} people'


class Booking(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #settings have authUsermodel,
    room=models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in=models.DateTimeField()
    check_out=models.DateTimeField()

    def __str__(self):
        return f'{self.user} has booked {self.room} from {self.check_in} to {self.check_out}'



    


