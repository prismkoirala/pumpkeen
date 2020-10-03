from django.db import models

class OilType(models.Model):
    name = models.CharField(max_length=100, default="-")
    price = models.DecimalField(decimal_places=2, max_digits=5)

    def __str__(self):
        return self.name

class Billing(models.Model):

    oil = models.ForeignKey(OilType, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="-")
    quantity = models.IntegerField(default=1, null=False, blank=False )
    time = models.DateTimeField(auto_now_add=True)

    def get_total(self):
        tot = self.oil.price * self.quantity
        return tot
# Create your models here.
