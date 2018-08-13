from django.db import models
from django.shortcuts import reverse

from .data_choices import it as io_types
from .data_choices import rt as record_types

# Create your models here.

def custom_path(instance, filename):
    arr = [choice(string.ascii_letters) for _ in range(8)]
    pid = ''.join(arr)
    extension = filename.split('.')[-1]
    date = timezone.now()
    return 'image/%s/%s/%s/%s.%s' % (
        date.year,
        date.month,
        date.day,
        pid,
        extension,
    )

class Record(models.Model):
    patient = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    io_type = models.PositiveIntegerField(choices=io_types)
    record_type = models.PositiveIntegerField(choices=record_types)
    amount = models.FloatField()
    registered_time = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('record-detail', kwargs={'pk': self.pk})


class FoodList(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to=custom_path)
    count = models.FloatField(default=0)
    amount = models.PositiveIntegerField(default=0)