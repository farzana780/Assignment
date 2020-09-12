from django import forms
from .models import pipe

class pipeform(forms.ModelForm):
    class Meta:
        model = pipe
        fields = ['Pipe_Outside_Diameter', 'Pipe_Wall_Thickness', 'Pipe_Density', 'Corrosion_Allowance',
                  'Coating_No', 'Description', 'External_Coating_Thickness', 'Density', 'Installation_Empty',
                  'Flooded', 'Hydrotest']
