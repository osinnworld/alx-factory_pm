import logging
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Count, Q, Sum
from django.utils import timezone
from datetime import timedelta
from .mixins import UserIsOwnerMixin
from .models import ProblemReported, Report, ProductionLine, ProblemCategory
from .forms import ProblemReportedForm, ReportForm

logger = logging.getLogger(__name__)

class ReportListView(LoginRequiredMixin, ListView):
    model = Report
    template_name = 'reports/report_list.html'
    context_object_name = 'reports'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        production_line = self.request.GET.get('production_line')
        if production_line:
            queryset = queryset.filter(production_line__name=production_line)
        return queryset.order_by('-day')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['production_lines'] = ProductionLine.objects.all()
        return context

class ReportDetailView(LoginRequiredMixin, DetailView):
    model = Report
    template_name = 'reports/report_detail.html'
    context_object_name = 'report'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['problems'] = ProblemReported.objects.filter(report=self.object)
        context['problem_form'] = ProblemReportedForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ProblemReportedForm(request.POST)
        if form.is_valid():
            problem = form.save(commit=False)
            problem.user = request.user
            problem.report = self.object
            problem.save()
            messages.success(request, 'Problem reported successfully.')
            return redirect('reports:report-detail', pk=self.object.pk)
        else:
            context = self.get_context_data(object=self.object)
            context['problem_form'] = form
            return self.render_to_response(context)

class ReportCreateView(LoginRequiredMixin, CreateView):
    model = Report
    form_class = ReportForm
    template_name = 'reports/report_form.html'
    success_url = reverse_lazy('reports:dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        try:
            response = super().form_valid(form)
            messages.success(self.request, 'Report created successfully.')
            logger.info(f"Report created: ID={self.object.id}, User={self.request.user.username}, Date={self.object.day}, Product={self.object.product}")
            return response
        except Exception as e:
            logger.error(f"Error saving report: {str(e)}", exc_info=True)
            messages.error(self.request, f'Error creating report: {str(e)}')
            return self.form_invalid(form)

class ReportUpdateView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = Report
    form_class = ReportForm
    template_name = 'reports/report_form.html'
    success_url = reverse_lazy('reports:dashboard')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Report updated successfully.')
        return response

class ReportDeleteView(LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    model = Report
    template_name = 'reports/report_confirm_delete.html'
    success_url = reverse_lazy('reports:dashboard')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Report deleted successfully.')
        return super().delete(request, *args, **kwargs)

class ProblemUpdateView(LoginRequiredMixin, UpdateView):
    model = ProblemReported
    fields = ['status', 'priority']
    template_name = 'reports/problem_update_form.html'

    def get_success_url(self):
        return reverse_lazy('reports:report-detail', kwargs={'pk': self.object.report.pk})

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Problem updated successfully.')
        return response

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'reports/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        thirty_days_ago = timezone.now() - timedelta(days=30)

        recent_reports = Report.objects.filter(
            day__gte=thirty_days_ago,
            user=self.request.user
        ).order_by('-day')[:10]

        context['recent_reports'] = recent_reports

        user_reports = Report.objects.filter(user=self.request.user, day__gte=thirty_days_ago)
        
        context['production_lines'] = ProductionLine.objects.annotate(
            report_count=Count('reports', filter=Q(reports__day__gte=thirty_days_ago, reports__user=self.request.user)),
            problem_count=Count('reports__problemreported', filter=Q(reports__day__gte=thirty_days_ago, reports__user=self.request.user))
        )

        context['problem_stats'] = {
            'total': ProblemReported.objects.filter(report__in=user_reports).count(),
            'by_priority': ProblemReported.objects.filter(report__in=user_reports).values('priority').annotate(count=Count('id')),
            'by_status': ProblemReported.objects.filter(report__in=user_reports).values('status').annotate(count=Count('id')),
        }

        context['overall_performance'] = {
            'total_reports': user_reports.count(),
            'total_plan': user_reports.aggregate(total_plan=Sum('plan'))['total_plan'] or 0,
            'total_execution': user_reports.aggregate(total_execution=Sum('execution'))['total_execution'] or 0,
        }

        return context

class ProblemCategoryListView(LoginRequiredMixin, ListView):
    model = ProblemCategory
    template_name = 'reports/problem_category_list.html'
    context_object_name = 'categories'

class ProblemCategoryDetailView(LoginRequiredMixin, DetailView):
    model = ProblemCategory
    template_name = 'reports/problem_category_detail.html'

class ProblemCategoryCreateView(LoginRequiredMixin, CreateView):
    model = ProblemCategory
    fields = ['name', 'description']
    template_name = 'reports/problem_category_form.html'
    success_url = reverse_lazy('reports:problem-category-list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Problem category created successfully.')
        return response

class ProblemCategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = ProblemCategory
    fields = ['name', 'description']
    template_name = 'reports/problem_category_form.html'
    success_url = reverse_lazy('reports:problem-category-list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Problem category updated successfully.')
        return response

class ProblemCategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = ProblemCategory
    template_name = 'reports/problem_category_confirm_delete.html'
    success_url = reverse_lazy('reports:problem-category-list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Problem category deleted successfully.')
        return super().delete(request, *args, **kwargs)