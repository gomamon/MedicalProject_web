from rest_framework import serializers

from records.serializers import RecordSerializer

from .models import Information

# Create your serializers here.


class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = ('pk', 'pid', 'name', 'birth')


class InformationDetailSerializer(serializers.ModelSerializer):
    records = RecordSerializer(read_only=True, many=True)

    class Meta:
        model = Information
        fields = ('pk', 'pid', 'name', 'birth', 'records')
