from rest_framework import serializers
from gestione_ordini.models import Cliente, Ordine, OrdineDettaglio
from gestione_ristoranti.serializers import RistoranteSerializer, PiattoSerializer

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"

class OrdineSerializer(serializers.ModelSerializer):
    #cliente_id = ClienteSerializer(many=False, read_only=True)
    #ristorante_id = RistoranteSerializer(many=False, read_only=True)
    testata = serializers.SerializerMethodField()

    class Meta:
        model = Ordine
        fields = "__all__"
        #fields = ["id", "data_ora", "stato", "cliente_id", "ristorante_id", "testata"]

    def get_testata(self, obj):
        return f"ordine #{obj.id} [{obj.data_ora.date()}] - {obj.ristorante_id.nome} - {obj.cliente_id.nome}"

class OrdineDettaglioSerializer(serializers.ModelSerializer):
    ordine_id = OrdineSerializer(many=False, read_only=True)
    piatto_id = PiattoSerializer(many=False, read_only=True)

    class Meta:
        model = OrdineDettaglio
        fields = ["id", "ordine_id", "piatto_id", "quantita"]