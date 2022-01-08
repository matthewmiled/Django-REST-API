from django.db import models

'''
class Room(models.Model):
    room_name = models.CharField(max_length=200)

    def __str__(self):
        return self.room_name
'''

class Device(models.Model):
    device_identifier = models.CharField(max_length=200, unique=True)
    device_name = models.CharField(max_length=200)
    ip = models.CharField(max_length=200)
    room = models.CharField(max_length=200) #models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.device_name