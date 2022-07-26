from django.contrib import admin
from django.urls import path
from relatives.views import add_relatives, list_relatives
from mvtFamiliares.views import hello_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_page, name="hello"),
    path('add_relatives/', add_relatives, name="add_relatives"),
    path('list_relatives/', list_relatives, name="list_relatives")
]
