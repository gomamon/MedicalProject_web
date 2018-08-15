from django.db import models
from django.shortcuts import reverse

# Create your models here.


class Information(models.Model):
    pid = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=10)
    room = models.CharField(max_length=10)
    birth = models.DateField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('patient-detail', kwargs={'pk': self.pk})
