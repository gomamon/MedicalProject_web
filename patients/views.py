from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.views.generic import DetailView
#from django.views.generic import DetailDateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.models import User

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
        information = Information.objects.select_related('patient__information')
        context['information'] = information
        return context



class PatientDetailView(DetailView):
    template_name = 'patients/pages/detail.html'
    model = Information
    context_object_name = 'patient'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        records = Record.objects.filter(patient=context['patient'].patient).order_by('-registered_time')
        context['records'] = records
        return context


######## yeddo ####

class PatientDetailDateView(DetailView):
    template_name = 'patients/pages/detail_date.html'
    model = Information
    context_object_name = 'patient'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        records = Record.objects.filter(patient=context['patient'].patient).order_by('-registered_time')
        context['records'] = records
        return context

################



class PatientCreateView(CreateView):
    template_name = 'patients/forms/information.html'
    model = Information
    fields = ('pid', 'name', 'birth')

    def form_valid(self, form):
        patient = form.save(commit=False)
        patient.patient = User.objects.create(username=patient.pid, password=patient.pid)
        patient.save()
        return redirect('patients-main')





class PatientUpdateView(UpdateView):
    template_name = 'patients/forms/update.html'
    model = Information
    fields = ('pid', 'name', 'birth')
    ####yeddo
    def form_valid(self,form):
        patient = form.save(commit=False)
        patient.patient = User.objects.create(username=patient.pid, password=patient.pid)
        patient.save()
        return redirect('patient-main')



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
        queryset.records = Record.objects.filter(patient=queryset.patient)
        serializer = InformationDetailSerializer(queryset)
        return Response(serializer.data)
