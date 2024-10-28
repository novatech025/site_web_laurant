from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "main/index.html")

def contact(request):
    return render(request,"main/contact.html")
def erreur_404(request,exception):
    return render(request,"main/404.html",status=404) # gestion des page not found
