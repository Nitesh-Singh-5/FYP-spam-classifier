from django.db import models

# Create your models here.

class Form_Message(models.Model):
    message = models.CharField(max_length=255)
    result = models.CharField(max_length=255)
    accuracy = models.FloatField(max_length=255)

    def __str__(self):
        return self.message

CHOICES = (
    ('SPAM','SPAM'),
    ('HAM','HAM'),
)

class Feedback_Model(models.Model):
    message = models.CharField(max_length=255)
    our_prediction = models.CharField(max_length=255)
    your_prediction = models.CharField(choices=CHOICES,max_length=50)

    def __str__(self):
        return self.message