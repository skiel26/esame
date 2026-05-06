from rest_framework import serializers
from gestione_ristoranti.models import Tipologia, Ristorante, Piatto

class TipologiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipologia
        fields = "__all__"

class RistoranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ristorante
        fields = ["id", "nome", "telefono", "tipologia_id"]

class PiattoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piatto
        fields = "__all__"