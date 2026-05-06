from django.contrib import admin
from gestione_ordini.models import Cliente, Ordine, OrdineDettaglio

admin.site.register(Cliente)
admin.site.register(Ordine)
admin.site.register(OrdineDettaglio)

