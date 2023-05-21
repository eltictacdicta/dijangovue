
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('listelement.urls')),
    path('comment/',include('comment.urls') ),
    path("accounts/", include("account.urls")),
    path("accounts/", include("django.contrib.auth.urls"))
]
