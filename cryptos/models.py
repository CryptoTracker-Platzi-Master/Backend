from django.db import models
from django.contrib.auth.models import User
from datetime import date
today = date.today()
# Create your models here.
class Criptos(models.Model):
    id_c = models.AutoField(primary_key=True)    
    name = models.CharField(max_length=200)    
    purchase_price = models.FloatField()
    take_profit = models.FloatField()
    stop_loss = models.FloatField()
    cantity = models.FloatField()
    able = models.IntegerField(default=1)
    date_purchase = models.DateField(default=today) 
    user_fk = models.ForeignKey(User, on_delete=models.PROTECT)
    
    class Meta:
        ordering = ('id_c',)
        db_table = 'criptos'

    def __str__(self):
        return self.name