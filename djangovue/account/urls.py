
from django.urls import path
from .views import user_data,profile,register
app_name='account'
urlpatterns = [
    path('user_data/', user_data, name="user_data"),
    path('profile/', profile, name="profile"),
    path('register/', register, name="register")
]
