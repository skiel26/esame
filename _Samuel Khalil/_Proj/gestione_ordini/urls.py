from django.urls import path, include
from rest_framework.routers import DefaultRouter
from gestione_ordini.views import OrdineViewSet

router = DefaultRouter()
router.register(r'ordini', OrdineViewSet)

urlpatterns = [
    path('', include(router.urls)),
]