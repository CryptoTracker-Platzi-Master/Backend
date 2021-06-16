from django.db import models

# Create your models here.
class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'



class Criptos(models.Model):
    id_c = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    purchase_price = models.FloatField()
    take_profit = models.FloatField()
    stop_loss = models.FloatField()
    cantity = models.FloatField()
    able = models.IntegerField()
    date_purchase = models.DateField()
    img = models.CharField(max_length=200)
    user_fk = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='user_fk')

    class Meta:
        managed = False
        db_table = 'criptos'