from django.contrib import admin
from django.urls import path
from .views import analyze_scope

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/analyze/', analyze_scope, name='analyze_scope'),
]