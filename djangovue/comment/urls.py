
from django.urls import path
from .views import add, index

urlpatterns = [
    path('', index, name="indexcomment"),
    path('add', add, name="addcomment"),
]
