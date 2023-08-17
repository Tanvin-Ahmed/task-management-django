from django.shortcuts import redirect, render
from django.views.generic import DeleteView, UpdateView, ListView, CreateView
from django.urls import reverse_lazy
from task_app.forms import TodoForm
from task_app.models import TaskModel
# Create your views here.
def home(request):
    return render(request, 'home.html')


class TaskFormView(CreateView):
    model = TaskModel
    template_name = 'task_form.html'
    form_class = TodoForm
    success_url = reverse_lazy('tasks')

class ViewTaskList(ListView):
    template_name = 'show_tasks.html'
    model = TaskModel
    context_object_name = 'data'
    ordering = ['id']
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_completed=False)
        return queryset


class ViewCompleteTaskList(ListView):
    template_name = 'completed_tasks.html'
    model = TaskModel
    context_object_name = 'data'
    ordering = ['id']
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_completed=True)
        return queryset

class EditTask(UpdateView):
    model = TaskModel
    form_class = TodoForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('tasks')


class UpdateStatusToCompleted(UpdateView):
    model = TaskModel
    fields = ['is_completed']
    success_url = reverse_lazy('completed_tasks')
    template_name = 'task_form.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_completed = not self.object.is_completed
        self.object.save()
        data = {'status': self.object.is_completed}
        return redirect(self.get_success_url())

class UpdateStatusToInCompleted(UpdateView):
    model = TaskModel
    fields = ['is_completed']
    success_url = reverse_lazy('tasks')
    template_name = 'task_form.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_completed = not self.object.is_completed
        self.object.save()
        data = {'status': self.object.is_completed}
        return redirect(self.get_success_url())

class DeleteTask(DeleteView):
    model = TaskModel
    success_url = reverse_lazy('tasks')
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.get_success_url())

class DeleteCompletedTask(DeleteView):
    model = TaskModel
    success_url = reverse_lazy('completed_tasks')
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.get_success_url())