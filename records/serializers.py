from rest_framework import serializers

from .models import Record

# Create your serializers here.
class RecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Record
        fields = ('patient', 'io_type', 'record_type', 'amount', 'registered_time',)


class RecordListSerializer(serializers.ModelSerializer):
    patient_pid = serializers.CharField(source='patient.pid')
    patient_name = serializers.CharField(source='patient.name')
    io_type = serializers.CharField(source='get_io_type_display')
    record_type = serializers.CharField(source='get_record_type_display')

    class Meta:
        model = Record
        fields = ('patient_pid', 'patient_name', 'io_type', 'record_type', 'amount', 'registered_time',)
