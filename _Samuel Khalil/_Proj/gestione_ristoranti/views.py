from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from gestione_ristoranti.models import Tipologia, Ristorante, Piatto
from gestione_ristoranti.serializers import TipologiaSerializer, RistoranteSerializer, PiattoSerializer

class TipologiaViewSet(viewsets.ModelViewSet):
    queryset = Tipologia.objects.all()
    serializer_class = TipologiaSerializer

    @action(methods=['GET'], detail=False)
    def tipologie(self, request, pk=None):
        tipologie = self.get_object().all()
        return Response(TipologiaSerializer(tipologie, many=True).data)

    @action(methods=['GET'], detail=True)
    def ristoranti(self, request, pk=None):
        tipologia = self.get_object()
        ristoranti = tipologia.ristoranti.all()
        return Response(RistoranteSerializer(ristoranti, many=True).data)

class RistoranteViewSet(viewsets.ModelViewSet):
    queryset = Ristorante.objects.all()
    serializer_class = RistoranteSerializer

    @action(methods=['GET'], detail=False)
    def ristoranti(self, request, pk=None):
        ristoranti = self.get_object().all()
        return Response(RistoranteSerializer(ristoranti, many=True).data)

    @action(methods=['GET'], detail=True)
    def menu(self, request, pk=None):
        ristorante = self.get_object()
        piatti = ristorante.piatti.all()
        return Response(PiattoSerializer(piatti, many=True).data)

class PiattoViewSet(viewsets.ModelViewSet):
    queryset = Piatto.objects.all()
    serializer_class = PiattoSerializer

    @action(methods=['POST'], detail=True)
    def piatti(self, request, pk=None):
        ristorante = self.get_object()
        id_piatto = request.data.get('id')
        if not id_piatto:
            return Response({"error": "ID mancante"}, status=status.HTTP_400_BAD_REQUEST)
        piatto = get_object_or_404(Piatto, pk=id_piatto)
        ristorante.piatti.add(piatto)
        return Response({"status": "ok"})




