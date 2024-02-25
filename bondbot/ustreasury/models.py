from django.db import models

class Account(models.Model):
    owner_name = models.CharField(max_length=100)
    cash = models.DecimalField(max_digits=12, decimal_places=2)

class BondType(models.Model):
    ticker = models.CharField(max_length=10)
    maturity_length = models.DurationField()
    bc_cat = models.CharField(max_length=15)

class DailyBond(models.Model):
    bond_type = models.ForeignKey(BondType, on_delete=models.CASCADE)
    day = models.DateField()
    price = models.DecimalField(max_digits=7, decimal_places=4)
    yield_rate = models.DecimalField(max_digits=5, decimal_places=2)

class HeldBond(models.Model):
    daily_bond = models.ForeignKey(DailyBond, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()


    
