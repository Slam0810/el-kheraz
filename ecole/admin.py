
from django.contrib import admin

# Register your models here.

from .models import  Offre, Review, Person


admin.site.register(Offre)

admin.site.register(Review)

admin.site.register(Person)