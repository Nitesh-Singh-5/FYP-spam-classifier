from django.db import models

# Create your models here.

class Form_Message(models.Model):
    message = models.CharField(max_length=255)
    result = models.CharField(max_length=255)
    accuracy = models.FloatField(max_length=255)

    def __str__(self):
        return self.message