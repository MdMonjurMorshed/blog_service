from django.db import models

# Create your models here.

class User(models.Model):
    uuid = models.UUIDField(max_length=124,auto_created=True,primary_key=True,db_index=True)
    first_name = models.CharField(max_length=50,null=False)
    middle_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=False)
    avatar = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=100,null=False)
    phone_number = models.CharField(max_length=100,null=True)
    

    

