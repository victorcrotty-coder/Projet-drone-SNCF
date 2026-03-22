from django.contrib import admin

from .models import Contact, Accueil, Mission, Drone, Station, Donnees, Message

admin.site.register(Contact)
admin.site.register(Accueil)
admin.site.register(Mission)
admin.site.register(Drone)
admin.site.register(Station)
admin.site.register(Donnees)
admin.site.register(Message)
