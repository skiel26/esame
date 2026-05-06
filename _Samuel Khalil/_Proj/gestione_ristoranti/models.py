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
    ristorante_id = models.ForeignKey(
        Ristorante,
        null=True,
        on_delete=models.CASCADE,
        related_name="piatti"
    )

    def __str__(self):
        return self.nome