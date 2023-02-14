from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Task

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'
    paginate_by = 10

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'task_form.html'
    fields = ['title', 'description', 'due_date']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'task_form.html'
    fields = ['title', 'description', 'due_date']

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task_confirm_delete.html'
    success_url = reverse_lazy('tasks')

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


@login_required
def home(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'home.html', {'tasks': tasks})

@login_required
def add_task(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        task_obj = Task(name=name, description=description, user=request.user)
        task_obj.save()
        return redirect('home')
    return render(request, 'add_task.html')

@login_required
def edit_task(request, task_id):
    task_obj = Task.objects.get(id=task_id)
    if task_obj.user != request.user:
        return redirect('home')
    if request.method == 'POST':
        task_obj.task = request.POST['task']
        task_obj.save()
        return redirect('home')
    return render(request, 'edit_task.html', {'task': task_obj.task})

@login_required
def delete_task(request, task_id):
    task_obj = Task.objects.get(id=task_id)
    if task_obj.user != request.user:
        return redirect('home')
    task_obj.delete()
    return redirect('home')