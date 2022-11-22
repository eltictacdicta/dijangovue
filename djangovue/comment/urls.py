
from django.urls import path
from .views import add, index, update, contact

app_name='comment'
urlpatterns = [
    path('', index, name="index"),
    path('add', add, name="add"),
    path('contact', contact, name="contact"),
    path('update/<int:pk>', update, name="update"),
]
