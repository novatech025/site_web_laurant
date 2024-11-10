from django.shortcuts import render
from .models import *
from django.core.mail import mail_admins
from django.contrib import messages

def index(request):
    testimony_list = Testimonial.objects.filter(published=True)[:6]
    context = {
        'title': 'Accueil | QUALISABLE',
        "selected_tab": "home",
        "testimony_list": testimony_list
    }

    return render(request, "main/index.html",context)

def privacy_policy(request):
    context = {
        'title': 'Politique de confidentialité | QUALISABLE',
    }

    return render(request, "main/privacy-policy.html",context)

def legal_mention(request):
    context = {
        'title': 'Mentions légales | QUALISABLE',
    }

    return render(request, "main/legal-mention.html",context)

def contact(request):
    if request.POST:
        name = request.POST.get('nom')
        email = request.POST.get('mail')
        message = request.POST.get('message')
        new_message_user = Message_User.objects.create(name = name, email = email, message = message)
        new_message_user.save()
        
        # print(name)
        # print(email)
        # print(message)
        
        sujet = "message aux adminitrateur du site de qualisable"
        corps_message = f"""
                Nom: {name}
                Email: {email}
                Message: {message}
            """

            # Envoyer le message email aux administrateurs
        mail_admins(
            subject=sujet,
            message=corps_message,
        )
        messages.error(request, "message  envoyer avec succes")
    context = {
        'title': 'Nos Contacts',
        "selected_tab": "contact",
    }
    return render(request,"main/contact.html",context)

def service(request):
    services = Service.objects.all()
    context = {
        'services': services,
        'title': 'Nos Services',
        "selected_tab": "services",
    }
    return render(request,"main/services.html",context)

def realisation(request):
    realisations = Realisation.objects.all()
    context = {
        'realisations': realisations,
        'title': 'Nos Realisations',
        "selected_tab": "realisations",
    }
    return render(request,"main/realisations.html",context)

def erreur_404(request, exception):
    return render(request,"main/404.html",status=404) # gestion des page not found
