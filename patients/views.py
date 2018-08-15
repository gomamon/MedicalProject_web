from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

##yeddo
from django.views.generic.edit import RecordsView
##
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.response import Response

from records.models import Record

from .models import Information
from .serializers import InformationSerializer
from .serializers import InformationDetailSerializer

# Create your views here.


class MainPatientView(TemplateView):
    template_name = 'patients/pages/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        information = Information.objects.all()
        context['information'] = information
        return context


class PatientDetailView(DetailView):
    template_name = 'patients/pages/detail.html'
    model = Information
    context_object_name = 'patient'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        records = Record.objects.filter(patient=context['patient']).order_by('-registered_time')
        context['records'] = records
        return context


class PatientDetailDateView(DetailView):
    template_name = 'patients/pages/detail_date.html'
    model = Information
    context_object_name = 'patient'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        records = Record.objects.filter(patient=context['patient']).order_by('-registered_time')
        context['records'] = records
        return context
##yeddo##

class PatientRecordsView(RecordsView):
    template_name = 'patients/forms/records.html'
    model = Information
    fields = ('pid', 'name', 'birth')

########
class PatientCreateView(CreateView):
    template_name = 'patients/forms/information.html'
    model = Information
    fields = ('pid', 'name', 'birth')


class PatientUpdateView(UpdateView):
    template_name = 'patients/forms/update.html'
    model = Information
    fields = ('pid', 'name', 'birth')


class PatientDeleteView(DeleteView):
    template_name = 'patients/confirm/information.html'
    model = Information
    success_url = reverse_lazy('patients-main')


class InformationViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, SessionAuthentication,)
    queryset = Information.objects.all()
    serializer_class = InformationSerializer

    def retrieve(self, request, pk):
        queryset = Information.objects.get(pk=pk)
        queryset.records = Record.objects.filter(patient=queryset.pid)
        serializer = InformationDetailSerializer(queryset)
        return Response(serializer.data)
