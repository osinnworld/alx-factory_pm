from django.urls import path
from .views import (
    ReportListView, ReportDetailView, ReportCreateView, ReportUpdateView, ReportDeleteView,
    ProblemUpdateView, DashboardView
)

app_name = 'reports'

urlpatterns = [
    path('', ReportListView.as_view(), name='report-list'),
    path('<int:pk>/', ReportDetailView.as_view(), name='report-detail'),
    path('new/', ReportCreateView.as_view(), name='report-create'),
    path('<int:pk>/edit/', ReportUpdateView.as_view(), name='report-update'),
    path('<int:pk>/delete/', ReportDeleteView.as_view(), name='report-delete'),
    path('problem/<int:pk>/update/', ProblemUpdateView.as_view(), name='problem-update'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]