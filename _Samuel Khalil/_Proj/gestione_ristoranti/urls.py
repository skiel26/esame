from django.urls import path, include
from rest_framework.routers import DefaultRouter
from gestione_ristoranti.views import TipologiaViewSet, RistoranteViewSet, PiattoViewSet

router = DefaultRouter()
router.register(r'tipologie', TipologiaViewSet)
router.register(r'ristoranti', RistoranteViewSet)
router.register(r'piatti', PiattoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]