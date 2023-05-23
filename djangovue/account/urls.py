
from django.urls import path
from .views import user_data,profile
app_name='comment'
urlpatterns = [
    path('user_data/', user_data, name="user_data"),
    path('profile/', profile, name="profile"),
]
