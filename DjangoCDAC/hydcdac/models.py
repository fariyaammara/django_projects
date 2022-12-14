
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# Create your models here.



class HydCdac(models.Model):
    joining_date = models.DateTimeField(auto_now_add=False,default='NAN')
    employee_name = models.CharField(max_length=100, blank=True, default='')
    age = models.IntegerField(default=0)
    place = models.CharField(max_length=100, blank=True, default='')
    class Meta:
        ordering = ['joining_date']


class HydCdacemp(models.Model):
    em_id=models.IntegerField() 
    pay=models.IntegerField()
    emp_name=models.CharField(max_length=100, blank=True, default='')
    emp_grp=models.CharField(max_length=20, blank=True, default='')
    class Meta:
        ordering = ['em_id']