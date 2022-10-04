
from django.urls import path
from .views import add, index, update

urlpatterns = [
    path('', index, name="indexcomment"),
    path('add', add, name="addcomment"),
    path('update/<int:pk>', update, name="updatecomment"),
]
