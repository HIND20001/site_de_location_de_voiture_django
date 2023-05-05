from django.shortcuts import render, redirect
from item.models import Cars
from item.models import types
from .forms import SingupForm
from django.contrib.auth import logout
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def index(request):
    car = Cars.objects.filter(is_reserved = False) [0:6]
    categories = types.objects.all()
    return render(request, 'core/index.html',{
        'car' :car,
        'categories' :categories,
    })
    

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST' :
        form = SingupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login')
    else:
        form = SingupForm()
    

    return render(request, 'core/signup.html', {
        'form':form
    })

def user_logout(request):
    logout(request)
    # Redirect to a success page
    return redirect('/''')


