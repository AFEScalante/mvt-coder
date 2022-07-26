from django.contrib import admin
from django.urls import path
from mvtFamiliares.views import hello_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_page)
]
