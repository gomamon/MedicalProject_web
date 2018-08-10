from rest_framework import serializers

from .models import Record

# Create your serializers here.
class RecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Record
        fields = ('patient', 'io_type', 'record_type', 'amount', 'registered_time',)


class RecordListSerializer(serializers.ModelSerializer):
    patient_pid = serializers.CharField(source='patient.information.pid')
    patient_name = serializers.CharField(source='patient.information.name')

    class Meta:
        model = Record
        fields = ('patient_pid', 'patient_name', 'io_type', 'record_type', 'amount', 'registered_time',)
