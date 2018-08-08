from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Record(models.Model):
    patient = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    registered_time = models.DateTimeField(auto_now=True)
    liquid_amount = models.FloatField()
    consume_amount = models.FloatField()
    urine_amount = models.FloatField()
    stool_count = models.PositiveIntegerField()

    def get_absolute_url(self):
        return reverse('record-detail', kwargs={'pk': self.pk})
