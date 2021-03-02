from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Developer
from django.http import HttpResponse

def index(request):
    all_devs = Developer.objects.all()
    context = {
        'all_devs' : all_devs
    }
    return render(request, 'ninja/index.html', context)

def details(request, dev_id):
    dev = get_object_or_404(Developer, pk=dev_id)
    return render(request, 'ninja/details.html', {'dev':dev})