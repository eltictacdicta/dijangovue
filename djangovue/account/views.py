from django.shortcuts import render

# Create your views here.
def user_data(request):
    print(request.user.username)
    return render(request,'account/user_data.html')
