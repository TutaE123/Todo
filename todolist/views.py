from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import ToDo
from .log_utils import log_event


def index(request):
    todos = ToDo.objects.all()
    return render(request, 'todoapp/index.html', {'todo_list': todos, 'title': 'Главная страница'})

@require_http_methods(['POST'])
@csrf_exempt
def add(request: HttpRequest):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            todo = ToDo(title=title)
            todo.save()
            log_event('create_logger', f'Новая задача создана: {title}')
            messages.success(request, "Задание успешно создано")
        else:
            messages.warning(request, "Заголовок задания должен быть заполнен")
    return redirect('index')

def update(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.is_complete = not todo.is_complete
    todo.save()

    status = "Закрыто" if todo.is_complete else "Открыто"
    log_event('update_logger', f'Задача "{todo.title}" была {status}')

    return redirect('index')

def delete(request: HttpRequest, todo_id: int):
    todo = ToDo.objects.get(id=todo_id)
    if request.method == 'POST':
        log_event('delete_logger', f'Удаление задачи: {todo.title}')
        todo.delete()
        messages.success(request, "Задание успешно удалено")
    return redirect('index')

""" 
def redact(request, todo_id: int):
    todo = ToDo.objects.get(id = todo_id)
    if request.method == 'POST':
        form = ToDoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('task_detail', todo_id=todo_id)
        else:
            form = ToDoForm(instance=todo)
        
        return render(request, 'edit_task.html', {'form': form}) """