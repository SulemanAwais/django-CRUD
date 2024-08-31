from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib import messages
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from playground.models import Task


class RootView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/landing_page/')
        return render(request, 'root/index.html')


class ListDummyUsersView(View):
    def get(self, request):
        users = [
            {'name': 'Suleman', 'age': 22, 'is_male': True},
            {'name': 'Salma', 'age': 21, 'is_male': False},
            {'name': 'Idrees', 'age': 33, 'is_male': False},
        ]
        return render(request, 'hello.html', {'users': users})


class LandingPageView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'landing_page/index.html'
    context_object_name = 'tasks'
    login_url = '/login/'

    def get_queryset(self):
        return Task.objects.all()


class CreateTaskView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'content']
    template_name = 'create_task/index.html'
    login_url = '/login/'

    def form_valid(self, form):
        title = form.cleaned_data.get('title')
        content = form.cleaned_data.get('content')
        if not title and not content:
            messages.warning(self.request, "At least one field needs to be filled")
            return redirect('/create-task/')
        return super().form_valid(form)


class UpdateTaskView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'content']
    template_name = 'update_task/index.html'
    login_url = '/login/'
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        title = form.cleaned_data.get('title')
        content = form.cleaned_data.get('content')
        if not title and not content:
            messages.warning(self.request, "At least one field needs to be filled")
            return redirect(f'/update-task/{self.kwargs["id"]}')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('landing_page')


class DeleteTaskView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'landing_page/index.html'
    login_url = '/login/'
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse('landing_page')


class RegisterView(View):
    def get(self, request):
        return render(request, 'register/index.html')

    def post(self, request):
        try:
            data = request.POST
            email = data.get('email')
            password = data.get('password')
            username = data.get('username')
            if User.objects.filter(username=username).exists():
                messages.warning(request, 'Username should be unique')
                return redirect('/register/')
            if User.objects.filter(email=email).exists():
                messages.warning(request, 'Email already exists')
                return redirect('/register/')
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            return redirect('/landing_page/')
        except Exception as error:
            return HttpResponse(error)


class LoginPageView(View):
    def get(self, request):
        return render(request, 'login/index.html')

    def post(self, request):
        try:
            data = request.POST
            username = data.get('username')
            password = data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('/landing_page/')
            messages.warning(request, 'Username or Password didn\'t match')
            return redirect('/login/')
        except Exception as error:
            return HttpResponse(error)


class LogoutPageView(View):
    def get(self, request):
        try:
            logout(request)
            return redirect('/')
        except Exception as error:
            return HttpResponse(error)


class MyProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'my_profile/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        # Fetch user details from the database
        context['username'] = user.username
        context['email'] = user.email
        # context['password'] = user.password  # Typically, you would not fetch or display the current password

        return context