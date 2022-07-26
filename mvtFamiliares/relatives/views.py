from multiprocessing import context
from django.shortcuts import render
from relatives.models import Relatives

# Añade familiares a la database
def add_relatives(request):
    new_relative = Relatives.objects.create(name = 'Tomás', age = 3)
    new_relative_2 = Relatives.objects.create(name = 'Lola', age = 7, nickname = "Gorda")
    new_relative_3 = Relatives.objects.create(name = 'Alberto', age = 15)
    context = {
        'new_relative' : new_relative,
        'new_relative_2' : new_relative_2,
        'new_relative_3' : new_relative_3
    }
    return render(request, 'add_relative.html', context=context)

def list_relatives(request):
    relatives = Relatives.objects.all()
    context = {
        'relatives' : relatives
    }
    return render(request, 'see_relatives.html', context=context)