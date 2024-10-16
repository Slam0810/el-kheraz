from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Offre, Review
from django.contrib.auth.models import User



class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError("Les mots de passe ne correspondent pas.")



class OffreForm(forms.ModelForm):
    class Meta:
        model = Offre
        fields = ['titre', 'description', 'type', 'duree', 'prix', 'image']



class ContactForm(forms.Form):
    nom = forms.CharField(
        label='Nom',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre nom'}),
        error_messages={'required': 'Veuillez entrer votre nom'}
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Votre email'}),
        error_messages={'required': 'Veuillez entrer votre adresse email', 'invalid': 'Veuillez entrer une adresse email valide'}
    )
    message = forms.CharField(
        label='Message',
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Votre message'}),
        error_messages={'required': 'Veuillez entrer votre message'}
    )

class ReviewForm(forms.ModelForm):
    class Meta:
        nom = forms.CharField(
        label='Nom',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre nom'}),
        error_messages={'required': 'Veuillez entrer votre nom'}
        ),
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.RadioSelect(choices=[(i, str(i)) for i in range(1, 6)]),
        }