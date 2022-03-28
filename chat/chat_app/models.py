from django.db import models
from rest_framework.authtoken.models import Token

# Create your models here.
class Room(models.Model):
  room_name = models.CharField(max_length=50)
  member_count = models.IntegerField(null=True, blank=True)
  token = models.ForeignKey(Token, on_delete=models.CASCADE)


  def __str__(self):
    return self.room_name

# Create your models here.
class Message(models.Model):
  room_name = models.ForeignKey(Room, on_delete=models.CASCADE)
  message = models.CharField(max_length=100)
  sender = models.CharField(max_length=50)

  def __str__(self):
    return self.message

class HaveAGroup(models.Model):
  token = models.ForeignKey(Token, on_delete=models.CASCADE,null=True, blank=True)
  room_name = models.ForeignKey(Room, on_delete=models.CASCADE,null=True, blank=True)
