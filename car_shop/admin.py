from django.contrib import admin
from .models import Marque, Vehicule, Contact

@admin.register(Vehicule)
class VehiculeAdmin(admin.ModelAdmin):
    list_display = ('titre', 'marque', 'prix', 'annee', 'est_disponible')
    list_filter = ('marque', 'energie', 'est_disponible')
    search_fields = ('titre', 'modele')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'vehicule', 'date_envoi')
    readonly_fields = ('nom', 'email', 'telephone', 'message', 'vehicule', 'date_envoi')

admin.site.register(Marque)
