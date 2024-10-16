from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Chef
from django.contrib.auth import login, authenticate
from .models import Offre, Review, Person
from .forms import OffreForm
from django.core.mail import send_mail
from .forms import OffreForm, ContactForm, ReviewForm  # Add ContactForm here
import matplotlib.pyplot as plt
from django.db.models import Count, Avg
import io
import urllib, base64
#from django.contrib.auth import login, authenticate
from .forms import SignUpForm

def index(request):
    context = 'Page',
    
    return render(request, 'ecole/index.html', {'context' : context})


def presentation(request):
    return render(request, 'ecole/presentation.html')



def dirigeants(request):
    
    dirigeants = Chef.objects.all()
    #Paginator = Paginator(dirigeants, 3) # On affiche 3 chef par page

    return render(request, 'ecole/dirigeants.html', {'dirigeants': dirigeants})



# La creation d'un offre

def creer_offre(request):
    if request.method == 'POST':
        form = OffreForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('liste_offres')
    else:
        form = OffreForm()
    return render(request, 'ecole/creer_offre.html', {'form': form})


# Affichage  d'une offre

def liste_offres(request):
    offres = Offre.objects.all()
    return render(request, 'ecole/liste_offres.html', {'offres': offres})



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(
                f'Message de {nom}',
                message,
                email,
                [''],  # Remplacez par votre adresse email
            )
            return render(request, 'ecole/contact_success.html')
    else:
        form = ContactForm()
    return render(request, 'ecole/contact.html', {'form': form})


def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('index')  # Redirige vers la page d'accueil après soumission
    else:
        form = ReviewForm()
    return render(request, 'ecole/add_review.html', {'form': form})

def enseignantes(request):
    persons = Person.objects.all()
    return render(request, 'ecole/person_list.html', {'persons': persons})


def inscription(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'ecole/inscription.html', {'form': form})