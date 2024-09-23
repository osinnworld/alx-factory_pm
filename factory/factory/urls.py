from django.contrib import admin
from django.urls import path, include
from .views import home # type: ignore

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('reports/', include('reports.urls')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
]