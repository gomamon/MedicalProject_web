from django.db import models

# Create your models here.

class Information(models.Model):
    patient = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    pid = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=10)
    birth = models.DateField()

    def __str__(self):
        return self.pid
