from django.urls import path
from .views import TaskListView, TaskDetailView, SignUpView
from .views import home, add_task, edit_task, delete_task

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', home, name='home'),
    path('add_task/', add_task, name='add_task'),
    path('edit_task/<int:task_id>', edit_task, name='edit_task'),
    path('delete_task/<int:task_id>', delete_task, name='delete_task'),
]
