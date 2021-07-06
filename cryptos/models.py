from django.db import models
from django.contrib.auth.models import User
from datetime import date
today = date.today()
# Create your models here.
class Criptos(models.Model):
    id_c = models.AutoField(primary_key=True)    
    name = models.CharField(max_length=200)
    symbol = models.CharField(max_length=200)
    purchase_price = models.FloatField()
    take_profit = models.FloatField()
    stop_loss = models.FloatField()
    cantity = models.FloatField()
    amount_invested = models.FloatField()
    able = models.IntegerField(default=1)
    date_purchase = models.DateField("Creation date", auto_now=False, auto_now_add=True)
    user_fk = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        managed = True
        ordering = ('id_c',)
        db_table = 'criptos'

    def __str__(self):
        return self.name

