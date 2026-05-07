from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from gestione_ordini.models import Cliente, Ordine, OrdineDettaglio
from gestione_ordini.serializers import ClienteSerializer, OrdineSerializer, OrdineDettaglioSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class OrdineViewSet(viewsets.ModelViewSet):
    queryset = Ordine.objects.all()
    serializer_class = OrdineSerializer

    @action(methods=['GET'], detail=False)
    def ordini(self, request, pk=None):
        ordini = self.get_object().all()
        return Response(OrdineSerializer(ordini, many=True).data)

    @action(methods=['POST'], detail=True)
    def ordini(self, request, pk=None):
        ristorante = self.get_object()
        cliente = self.get_object()
        id_ordine = request.data.get('id')
        if not id_ordine:
            return Response({"error": "ID mancante"}, status=status.HTTP_400_BAD_REQUEST)
        ordine = get_object_or_404(Ordine, pk=id_ordine)
        ristorante.ordini.add(ordine)
        cliente.ordini.add(ordine)
        return Response({"status": "ok"})

class OrdineDettaglioViewSet(viewsets.ModelViewSet):
    queryset = OrdineDettaglio.objects.all()
    serializer_class = OrdineDettaglioSerializer
