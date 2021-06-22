from datetime import datetime, timedelta
from django.db import models
from django.contrib.auth.models import User
import random

# Create your models here.
class Code(models.Model) :
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=6, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_used = models.BooleanField(default=0)
    address = models.CharField(max_length=15, null=True)
    expire_date = models.DateTimeField(blank=True)

    class Meta:
        ordering = ('id',)
        db_table = 'codes'

    def __str__(self):
        return self.code

    def codegen(self) -> str:
        nums = [x for x in range(10)]
        strcode = ''

        for x in range(6) :
            strcode += str(random.choice(nums))
        
        date = datetime.now()
        delta = timedelta(hours=1)
        
        self.is_used = 0
        self.code = strcode
        self.expire_date = date + delta

        return strcode