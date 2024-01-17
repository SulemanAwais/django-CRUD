
from django.shortcuts import render


# Create your views here.
def ems_root(request):
    return render(request=request, template_name='home_page/index.html')


def ems_login_page(request):
    return render(request=request, template_name='login_page/index.html')


def ems_register_page(request):
    return render(request=request, template_name='register_page/index.html')
