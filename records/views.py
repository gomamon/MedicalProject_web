from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.response import Response

from .models import Record
from .serializers import RecordSerializer
from .serializers import RecordListSerializer

# Create your views here.

class MainRecordView(TemplateView):
    template_name = 'records/pages/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        information = Record.objects.all().select_related('patient__information').order_by('-registered_time')
        context['information'] = information
        return context


class RecordDetailView(DetailView):
    template_name = 'records/pages/record.html'
    model = Record
    context_object_name = 'record'


class RecordCreateView(CreateView):
    template_name = 'records/forms/record.html'
    model = Record
    fields = ('patient', 'liquid_amount', 'consume_amount', 'urine_amount', 'stool_count',)


class RecordUpdateView(UpdateView):
    template_name = 'records/forms/record.html'
    model = Record
    fields = ('liquid_amount', 'consume_amount', 'urine_amount', 'stool_count',)


class RecordDeleteView(DeleteView):
    template_name = 'records/confirm/record.html'
    model = Record
    success_url = reverse_lazy('records-main')


class RecordViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, SessionAuthentication,)
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

    def list(self, request):
        queryset = Record.objects.all().select_related('patient__information')
        serializer = RecordListSerializer(queryset, many=True)
        return Response(serializer.data)
