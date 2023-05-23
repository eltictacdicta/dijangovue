from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def user_data(request):
    print(request.user.username)
    return render(request,'account/user_data.html')

@login_required
def profile(request):
    return render(request,'account/user_data.html')
