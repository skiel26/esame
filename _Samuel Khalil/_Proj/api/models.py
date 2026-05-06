from django.core.validators import MinValueValidator
from django.db import models

class Tipologia(models.Model):
    nome = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.nome

class Ristorante(models.Model):
    nome = models.CharField(max_length=100, null=False)
    telefono = models.CharField(max_length=20, null=True)
    tipologia_id = models.ForeignKey(
        Tipologia,
        on_delete=models.PROTECT,
        related_name="ristoranti"
    )

    def __str__(self):
        return self.nome

class Piatto(models.Model):
    nome = models.CharField(max_length=100, null=False)
    prezzo = models.DecimalField(max_digits=10, decimal_places=2, null=False)

    def __str__(self):
        return self.nome

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

    def __str__(self):
        questo_ristorante = self.ristorante_id
        return f"ordine {self.data_ora}"

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