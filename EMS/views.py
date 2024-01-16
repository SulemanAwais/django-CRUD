
from django.shortcuts import render


# Create your views here.
def ems_root(request):
    return render(request=request, template_name='home_page/index.html')
