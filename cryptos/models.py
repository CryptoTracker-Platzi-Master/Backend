from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Criptos(models.Model):
    id_c = models.AutoField(primary_key=True)
    id_api = models.IntegerField()
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='profile/photos',default='')
    purchase_price = models.FloatField()
    take_profit = models.FloatField()
    stop_loss = models.FloatField()
    cantity = models.FloatField()
    able = models.IntegerField()
    date_purchase = models.DateField()    
    user_fk = models.ForeignKey(User, on_delete=models.PROTECT)
    
    class Meta:
        ordering = ('id_c',)
        db_table = 'criptos'

    def __str__(self):
        return self.name