from django.urls import path, include
from django.contrib.auth.decorators import login_required

from rest_framework import routers

from .views import MainRecordView
from .views import RecordCreateView
from .views import RecordDetailView
from .views import RecordUpdateView
from .views import RecordDeleteView
from .views import RecordViewSet

# Create your urls here.

router = routers.DefaultRouter()
router.register('records-list', RecordViewSet, base_name='records_list')

urlpatterns = [
    path('', login_required(MainRecordView.as_view()), name='records-main'),
    path('new/', login_required(RecordCreateView.as_view()), name='record-new'),
    path('<pk>/detail/', login_required(RecordDetailView.as_view()), name='record-detail'),
    path('<pk>/update/', login_required(RecordUpdateView.as_view()), name='record-update'),
    path('<pk>/delete/', login_required(RecordDeleteView.as_view()), name='record-delete'),
    path('api/', include(router.urls)),
]
