from django.db import models


# Create your models here.
class pipe(models.Model):
    Pipe_Outside_Diameter = models.FloatField(default='10.75')
    Pipe_Wall_Thickness = models.FloatField(default='0.5')
    Pipe_Density = models.FloatField(default='490')
    Corrosion_Allowance = models.FloatField(default='0.125')
    Coating_No = models.IntegerField(default='1')
    Description = models.CharField(max_length=50, default='FBE')
    External_Coating_Thickness = models.FloatField(default='0.0118110236220472')
    Density = models.FloatField(default='81.156348')
    Installation_Empty = models.IntegerField(default='0')
    Flooded = models.FloatField(default='64')
    Hydrotest = models.FloatField(default='64.7')

