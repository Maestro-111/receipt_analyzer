from django.db import models


class Receipt(models.Model):
    image_id = models.IntegerField(primary_key=True)
    total = models.FloatField(blank=True, null=True, default=None)
    subtotal = models.FloatField(blank=True, null=True, default=None)
    store = models.TextField(blank=True, null=True)
    payment_type = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.image_id)

