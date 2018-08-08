from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import MainView as DashboardMainView

# Create your urls here.
urlpatterns = [
    path('', login_required(DashboardMainView.as_view()), name='dashboard-main'),
]
