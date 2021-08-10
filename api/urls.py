from django.urls import path
from .views import *



urlpatterns = [
    path('', apiOverview , name='home'),
    path('task-list/', taskList, name='task-list'),
    path('task-detail/<int:id>/', taskDetail, name='task-detail'),
    path('task-create/', taskCreate, name='task-create'),
    path('task-update/<int:id>/', taskUpdate, name='task-update'),
]