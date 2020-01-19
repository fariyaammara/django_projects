from django.db import models

# Create your models here.
class Employee(models.Model):#to tell that a class is model 
    eid = models.CharField(max_length=20)
    ename = models.CharField(max_length=1000)
    email=models.EmailField(max_length=1000)
    edateofbirth =models.CharField(max_length=1000)
    class Meta:
        db_table="employee"

    #meta class is a instance thouh which a class becomes a object
