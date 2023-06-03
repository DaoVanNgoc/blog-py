from django.shortcuts import render
from .forms import RegistrationForm
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
    return render(request,'pages/home.html')

def tintucbongda(request):
    return render(request,'pages/tintuc.html')
    
def contact(request):
    return render(request,'pages/contact.html')

# def handler404(request, exception):
#     return render(request,'pages/404.html')

# def handler404(request, exception):
#     return render(request,'pages/404.html')

# def handler500(request,):
#     return render(request,'pages/500.html')

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request,'pages/register.html', {'form':form})
