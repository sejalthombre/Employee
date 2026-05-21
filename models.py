from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    photo = models.BinaryField(blank=True, null=True)

    def __str__(self):
        return self.name