from django.urls import path
from .views import *



urlpatterns = [
    path('', apiOverview , name='home'),
    path('task-list/', taskList, name='task-list'),
]