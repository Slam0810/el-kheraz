from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('presentation/', views.presentation, name='presentation'),
    path('enseignantes/', views.enseignantes, name='enseignantes'),
    path('inscription/', views.inscription, name='inscription'),
    #path('liste_offres/', views.liste_offres, name='liste_offres'),
    path('liste_offres/', views.liste_offres, name='liste_offres'),
    path('creer_offre/', views.creer_offre, name='creer_offre'),
    path('contact/', views.contact, name='contact'),
    path('add_review/', views.add_review, name='add_review'),
    # Ajoute d'autres chemins ici
]