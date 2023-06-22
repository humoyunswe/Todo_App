from django.shortcuts import redirect,get_object_or_404
from django.views import generic
from .models import Todo

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'todo/index.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        return Todo.objects.order_by('-created_at')

def add(request):
    title = request.POST['title']
    Todo.objects.create(title=title)

    return redirect('todo:index')


def delete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.delete()

    return redirect('todo:index')

def update(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    isCompleted = request.POST.get('isCompleted',False)
    if isCompleted == 'on':
        isCompleted = True
    todo.isCompleted = isCompleted
    todo.save()
    return redirect('todo:index')


