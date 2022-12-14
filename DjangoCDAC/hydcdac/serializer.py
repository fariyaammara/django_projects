from rest_framework import serializers 
from hydcdac.models import HydCdac,HydCdacemp
 
 
class HydCdacSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = HydCdac
        fields = ('joining_date',
                  'employee_name',
                  'place',
                  'age')
        model = HydCdacemp
        fields=(
              'em_id',
                'pay',
                'emp_name',
                'emp_grp'
                )