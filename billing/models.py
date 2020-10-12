from django.db import models

class OilType(models.Model):
    name = models.CharField(max_length=100, default="-")
    price = models.DecimalField(decimal_places=2, max_digits=5)
    cp =  models.DecimalField(decimal_places=2, max_digits=5, default=100.5)
    stock =  models.DecimalField(decimal_places=2, max_digits=10, default=10000.50)

    def __str__(self):
        return self.name

class BillingHistory(models.Model):
    oil = models.ForeignKey(OilType, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="-")
    quantity = models.DecimalField(decimal_places=3, max_digits=7, default=1.00, null=True, blank=True )
    price = models.DecimalField(default=99.99, decimal_places=3, max_digits=7)
    amount = models.IntegerField(default=100, null=True, blank=True )
    time = models.DateTimeField(auto_now_add=True)
    profit = models.DecimalField(default=2.50, decimal_places=2, max_digits=9)
    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name
            
