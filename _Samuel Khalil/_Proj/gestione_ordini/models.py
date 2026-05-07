from django.core.validators import MinValueValidator
from django.db import models
from gestione_ristoranti.models import Tipologia, Ristorante, Piatto

class Cliente(models.Model):
    nome = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, unique=True)
    indirizzo = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.nome

class Ordine(models.Model):
    data_ora = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ("In elaborazione", "in elaborazione"),
        ("In preparazione", "in preparazione"),
        ("In transito", "in transito"),
        ("Consegnato", "consegnato")
    ]
    stato = models.CharField(max_length=50, choices=STATUS_CHOICES, default="In preparazione")
    cliente_id = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
        related_name="ordini"
    )
    ristorante_id = models.ForeignKey(
        Ristorante,
        on_delete=models.PROTECT,
        related_name="ordini"
    )

    testata = models.CharField(max_length=100, null=True, editable=False)

    def __str__(self):
        questo_ristorante = self.ristorante_id
        return f"ordine #{self.id} [{self.data_ora.date()}] - {self.ristorante_id.nome} - {self.cliente_id.nome}"



class OrdineDettaglio(models.Model):
    ordine_id = models.OneToOneField(Ordine, on_delete=models.CASCADE)
    piatto_id = models.ForeignKey(
        Piatto,
        on_delete=models.PROTECT,
        related_name="dettagli_ordine",
    )
    # quantita = models.IntegerField(null=False) # TODO: has to be higher than 0; reconsider if `null=False` equals `NOT NULL`
    quantita = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return f"ordine {self.ordine_id}_{self.piatto_id}"
