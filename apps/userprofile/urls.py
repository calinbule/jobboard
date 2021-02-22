from django.urls import path, include

from .views import dashboard, view_application, view_dashboard_job, profile

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('profile/', profile, name='profile'),
    path('job/<int:job_id>/', view_dashboard_job, name='view_dashboard_job'),
    path('application/<int:application_id>/', view_application, name='view_application'),
]