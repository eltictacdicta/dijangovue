from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def user_data(request):
    print(request.user.username)
    return render(request,'account/user_data.html')

@login_required
def profile(request):
    return render(request,'account/profile.html')


def register(request):
    form = UserCreationForm()
    return render(request,'account/register.html',{'form':form})
