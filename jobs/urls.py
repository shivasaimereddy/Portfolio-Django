from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('jobs/<int:job_id>', details, name='details'),
]
