from django.urls import path
from .views import TaskListView, TaskDetailView, SignUpView

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('signup/', SignUpView.as_view(), name='signup'),

]
