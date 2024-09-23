#REPORTS/ADMIN.PY

from django.contrib import admin
from .models import ProblemCategory, Report, ProblemReported

admin.site.register(Report)
admin.site.register(ProblemReported)
admin.site.register(ProblemCategory)
