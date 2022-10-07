
from django.urls import path
from .views import add, index, update, contact

urlpatterns = [
    path('', index, name="indexcomment"),
    path('add', add, name="addcomment"),
    path('contact', contact, name="indexcontact"),
    path('update/<int:pk>', update, name="updatecomment"),
]
