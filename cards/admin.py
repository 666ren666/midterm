from django.contrib import admin
from .models import UserProfile, Deck, Card

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Card)
admin.site.register(Deck)
