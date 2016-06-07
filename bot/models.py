from django.db import models
from django.utils import timezone

# Create your models here.
class Message(models.Model):
    text = models.TextField()
    sent_date = models.DateTimeField(
        default=timezone.now)
    #user = gen'd based on IP? Random Name? Requests name in early messages?

    def send(self):
        self.sent_date = timezone.now()
        self.save()

    def receive(self):
        self.sent_date = timezone.now()
