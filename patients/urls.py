from django.urls import path, include
from django.contrib.auth.decorators import login_required

from rest_framework import routers

from .views import MainPatientView
from .views import PatientDetailView
from .views import PatientCreateView
from .views import PatientUpdateView
from .views import PatientDeleteView
from .views import InformationViewSet
from .views import PatientDetailDateView
# Create your urls here.

router = routers.DefaultRouter()
router.register('patients-list', InformationViewSet, base_name='patients_list')

urlpatterns = [
    path('', login_required(MainPatientView.as_view()), name='patients-main'),
    path('new/', login_required(PatientCreateView.as_view()), name='patient-new'),
    path('<pk>/detail/', login_required(PatientDetailView.as_view()), name='patient-detail'),
    path('<pk>/update/', login_required(PatientUpdateView.as_view()), name='patient-update'),
    path('<pk>/delete/', login_required(PatientDeleteView.as_view()), name='patient-delete'),
    path('<pk>/detail_date/', login_required(PatientDetailDateView.as_view()), name='patient-detail-date'),
    path('api/', include(router.urls)),
]
