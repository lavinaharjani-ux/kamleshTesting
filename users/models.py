from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=255, default="jaipur")
    address_1 = models.CharField(max_length=255, default="jaipur")
    city = models.CharField(max_length=100, default="mp")


    def __str__(self):
        return self.name