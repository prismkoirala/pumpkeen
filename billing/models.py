from django.db import models

class OilType(models.Model):
    name = models.CharField(max_length=100, default="-")
    price = models.DecimalField(decimal_places=2, max_digits=5)

    def __str__(self):
        return self.name

class Billing(models.Model):
    oil = models.ForeignKey(OilType, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="-")
    quantity = models.IntegerField(default=1, null=True, blank=True )
    time = models.DateTimeField(auto_now_add=True)

    def get_total(self):
        tot = self.oil.price * self.quantity
        return tot

class BillingHistory(models.Model):
    oil = models.ForeignKey(OilType, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="-")
    quantity = models.DecimalField(decimal_places=2, max_digits=5, default=1.00, null=True, blank=True )
    price = models.DecimalField(default=99.99, decimal_places=2, max_digits=5)
    amount = models.IntegerField(default=100, null=True, blank=True )
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title
            
