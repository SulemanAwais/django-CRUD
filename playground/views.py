from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse
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


def landing_page(request, username):
    tasks_queryset = Task.objects.all()
    print(tasks_queryset)
    if tasks_queryset is not None:
        tasks = {'tasks': tasks_queryset,
                 'username': username}
        return render(request=request, template_name='landing_page/index.html', context=tasks)
    else:
        return render(request=request, template_name='landing_page/index.html', context={'username': username})


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


def update_task(request, id):
    try:
        task_id = int(id)
        if request.method == 'POST':
            data = request.POST
            title = data.get('title')
            content = data.get('content')
            print(title)
            print(task_id)
            #     print(type(task_id))
            #     print(content)
            task = Task.objects.get(id=id)
            if task:
                if title:
                    task.title = title
                if content:
                    task.content = content
            task.save()
            # return redirect(to='/')
            # return render(request=request, template_name='update_task/index.html', context={'id': id})
            landing_page_url = reverse(landing_page)
            return redirect(to=landing_page_url)

        else:
            return render(request=request, template_name='update_task/index.html', context={'id': id})
    except Exception as error:
        return HttpResponse(error)

    # return render(request=request, template_name='update_task/index.html')


def delete_task(request, id):
    try:
        task_id = int(id)
        print(task_id)
        task = Task.objects.get(id=id)
        if task:
            task.delete()
            return redirect(to='/')
        else:
            return HttpResponse('id does not exist')
    except Exception as error:
        return HttpResponse(error)


def register(request):
    try:
        if request.method == 'POST':
            data = request.POST
            email = data.get('email')
            password = data.get('password')
            username = data.get('username')
            user = User.objects.create(
                username=username,
                email=email,
            )
            user.set_password(password)
            user.save()
            landing_page_rul = reverse(viewname=landing_page, kwargs={'username': username})
            return redirect(to=landing_page_rul)
    except Exception as error:
        return HttpResponse(error)
    return render(request=request, template_name='register/index.html')


def login_page(request):
    return render(request=request, template_name='login/index.html')
