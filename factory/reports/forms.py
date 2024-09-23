from django import forms
from .models import Report, ProblemReported
from django.core.exceptions import ValidationError
from django.utils import timezone

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['day', 'start_hour', 'end_hour', 'product', 'plan', 'execution', 'production_line']
        widgets = {
            'day': forms.DateInput(attrs={'type': 'date'}),
            'start_hour': forms.Select(choices=Report.HOUR_CHOICES),
            'end_hour': forms.Select(choices=Report.HOUR_CHOICES),
        }

    def clean(self):
        cleaned_data = super().clean()
        day = cleaned_data.get('day')
        start_hour = cleaned_data.get('start_hour')
        end_hour = cleaned_data.get('end_hour')
        plan = cleaned_data.get('plan')
        execution = cleaned_data.get('execution')

        if day and day > timezone.now().date():
            raise ValidationError("Report date cannot be in the future.")

        if start_hour and end_hour and start_hour >= end_hour:
            raise ValidationError("End hour must be after start hour.")

        if plan and execution and execution > plan:
            raise ValidationError("Execution cannot exceed the plan.")

        return cleaned_data

class ProblemReportedForm(forms.ModelForm):
    class Meta:
        model = ProblemReported
        fields = ['category', 'description', 'breakdown', 'public', 'priority']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def clean_breakdown(self):
        breakdown = self.cleaned_data.get('breakdown')
        if breakdown and breakdown < 0:
            raise ValidationError("Breakdown value cannot be negative.")
        return breakdown