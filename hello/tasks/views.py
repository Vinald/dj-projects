from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from .forms import NewTaskForm


def tasks(request):
    if "TASKS" not in request.session:
        request.session['TASKS'] = []
    return render(request, 'tasks/tasks.html', {'tasks': request.session["TASKS"], 'title': 'Tasks'})


@csrf_protect
def add_task(request):
    if "TASKS" not in request.session:
        request.session['TASKS'] = []
    TASKS = request.session["TASKS"]
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            new_task = {
                'id': len(TASKS) + 1,
                'title': form.cleaned_data['title'],
                'description': form.cleaned_data['description'],
            }
            TASKS.append(new_task)
            request.session['TASKS'] = TASKS
            return render(request, 'tasks/tasks.html', {'tasks': TASKS, 'title': 'Tasks'})
        else:
            return render(request, 'tasks/add_task.html', {'form': form, 'title': 'Add Task'})

    return render(request, 'tasks/add_task.html', {'form': NewTaskForm()})
