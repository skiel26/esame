from rest_framework import serializers
from .models import Tipologia, Ristorante, Piatto, Cliente, Ordine, OrdineDettaglio

class TipologiaSerializer(serializers.ModelSerializer):
    class Meta:
        ...