from django.shortcuts import render, redirect
from django.http import HttpResponse

from playground.models import Task


# from playground.models import Task


def list_dummy_users(request):
    users = [
        {'name': 'Suleman', 'age': 22, 'is_male': True},
        {'name': 'Salma', 'age': 21, 'is_male': False},
        {'name': 'Idrees', 'age': 33, 'is_male': False},
    ]
    return render(request=request, template_name='hello.html', context={'users': users})


def landing_page(request):
    tasks_queryset = Task.objects.all()
    print(tasks_queryset)
    if tasks_queryset is not None:
        tasks = {'tasks': tasks_queryset}
        return render(request=request, template_name='landing_page/index.html', context=tasks)
    else:
        return render(request=request, template_name='landing_page/index.html')


def create_task(request):
    try:
        if request.method == 'POST':
            data = request.POST
            title = data.get('title')
            content = data.get('content')
            print(title)
            print(content)
            # date = data.get('title')
            Task.objects.create(
                title=title,
                content=content
            )
            return redirect(to='/')
    except Exception as error:
        return HttpResponse(error)
    return render(request=request, template_name='create_task/index.html')


def update_task(request):
    try:
        if request.method == 'POST':
            data = request.POST
            task_id = int(data.get('id')) - 1
            title = data.get('title')
            content = data.get('content')
            print(title)
            print(task_id)
            print(type(task_id))
            print(content)
            task = Task.objects.all()[task_id]
            if task:
                task.title = title
                task.content = content
                task.save()
                return redirect(to='/')
            else:
                return HttpResponse('id does not exist')
    except Exception as error:
        return HttpResponse(error)
    return render(request=request, template_name='update_task/index.html')


def delete_task(request):
    try:
        if request.method == 'POST':
            data = request.POST
            task_id = int(data.get('id')) - 1
            print(task_id)
            task = Task.objects.all()[task_id]
            if task:
                task.delete()
                return redirect(to='/')
            else:
                return HttpResponse('id does not exist')
    except Exception as error:
        return HttpResponse(error)
    return render(request=request, template_name='delete_task/index.html')



