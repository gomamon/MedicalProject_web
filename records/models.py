from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Record(models.Model):
    io_type = (
        (1, 'Input'),
        (2, 'Output'),
    )
    record_type_list = (
        (1, '수분'),
        (2, '식사'),
        (3, '소변'),
        (4, '대변'),
    )
    patient = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    io_type = models.PositiveIntegerField(choices=io_type)
    record_type = models.PositiveIntegerField(choices=record_type_list)
    amount = models.FloatField()
    registered_time = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('record-detail', kwargs={'pk': self.pk})
