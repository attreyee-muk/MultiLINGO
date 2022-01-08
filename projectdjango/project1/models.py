from django.db import models

from django.db import models


# Create your models here.
class ocr(models.Model):
    image = models.ImageField(upload_to='images/')
