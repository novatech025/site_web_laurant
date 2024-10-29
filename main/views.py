from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    context = {
        'title': 'QUALISABLE',
    }
    return render(request, "main/index.html",context)

def contact(request):
    context = {
        'title': 'Nos Contacts',
    }
    return render(request,"main/contact.html",context)
def service(request):
    services = Service.objects.all()
    context = {
        'services': services,
        'title': 'Nos Services',
    }
    return render(request,"main/services.html",context)
def realisation(request):
    realisations = Realisation.objects.all()
    context = {
        'realisations': realisations,
        'title': 'Nos Realisations',
    }
    return render(request,"main/realisations.html",context)
def erreur_404(request,exception):
    return render(request,"main/404.html",status=404) # gestion des page not found
