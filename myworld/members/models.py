from django.db import models

# Create your models here.
class Informatie(models.Model):
    city = models.CharField(max_length=255, blank=True, null=True)
    hotel = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Informatie'
        
    ##link csv file togehter put it in database 
   