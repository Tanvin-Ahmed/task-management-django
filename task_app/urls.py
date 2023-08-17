from django.urls import path
from task_app.views import (DeleteCompletedTask, DeleteTask, EditTask, home, TaskFormView,
    UpdateStatusToCompleted, UpdateStatusToInCompleted, ViewCompleteTaskList, ViewTaskList)

urlpatterns = [
    path('', home, name='home'),
    path('show_tasks/', ViewTaskList.as_view(), name='tasks'),
    path('show_completed_tasks/', ViewCompleteTaskList.as_view(), name='completed_tasks'),
    path('save_form/', TaskFormView.as_view(), name='save_form'),
    path('edit_task/<int:pk>', EditTask.as_view(), name='update_form'),
    path('update_task_complete/<int:pk>', UpdateStatusToCompleted.as_view(), name='update_to_complete'),
    path('update_task_incomplete/<int:pk>', UpdateStatusToInCompleted.as_view(), name='update_to_incomplete'),
    path('delete/<int:pk>', DeleteTask.as_view(), name='delete'),
    path('delete_completed_task/<int:pk>', DeleteCompletedTask.as_view(), name='delete_completed_task'),
]
