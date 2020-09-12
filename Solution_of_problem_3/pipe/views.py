from django.shortcuts import render, redirect
from .models import pipe
from .form import pipeform


# Create your views here.


def pipedetails(request):
    if request.method == 'POST':
        od = pipeform(request.POST)
        od.save()
        return redirect('pipe:calculation')
    else:
        value = pipeform()
        return render(request, 'pipe/index.html', {'value': value})


def calculation(request):

    data = pipe.objects.all()
    for i in data:
        Pipe_Outside_Radius = i.Pipe_Outside_Diameter / 2
        Pipe_Inside_Radius = (i.Pipe_Outside_Diameter - 2 * i.Pipe_Wall_Thickness) / 2
        Outer_Radius_of_Coating = Pipe_Outside_Radius + (i.External_Coating_Thickness / 2)
        Total_Pipeline_Outside_Diameter = Outer_Radius_of_Coating * 2
        Pipe_Weight_per_Unit_Length = 3.1416 * (((Pipe_Outside_Radius * Pipe_Outside_Radius) - (
            Pipe_Inside_Radius * Pipe_Inside_Radius)) / 144) * i.Pipe_Density
        Coating_1_Wt_per_Unit_Length_in_Air = 3.1416 * (((Outer_Radius_of_Coating * Outer_Radius_of_Coating) - (
            Pipe_Outside_Radius * Pipe_Outside_Radius)) / 144) * i.Density
        Contents_Wt_Per_Unit_Length_in_Air = 3.1416*((Pipe_Inside_Radius*Pipe_Inside_Radius)/144)*i.Installation_Empty
        Total_Weight_per_Unit_Length_in_Air = Pipe_Weight_per_Unit_Length + Coating_1_Wt_per_Unit_Length_in_Air
        Buoyant_Force_per_Unit_Length = 3.1416 * (
            (Outer_Radius_of_Coating * Outer_Radius_of_Coating) / 144) * i.Hydrotest
        Submerged_Weight_per_Unit_Length = Total_Weight_per_Unit_Length_in_Air - Buoyant_Force_per_Unit_Length
        Subm_Specific_Gravity_with_respect_to_SW = (Total_Weight_per_Unit_Length_in_Air / Buoyant_Force_per_Unit_Length)


    return render(request, 'pipe/calculation.html', {'Pipe_Outside_Radius': Pipe_Outside_Radius,
                                                     'Pipe_Inside_Radius': Pipe_Inside_Radius,
                                                     'Outer_Radius_of_Coating': Outer_Radius_of_Coating,
                                                     'Total_Pipeline_Outside_Diameter': Total_Pipeline_Outside_Diameter,
                                                     'Pipe_Weight_per_Unit_Length': Pipe_Weight_per_Unit_Length,
                                                     'Coating_1_Wt_per_Unit_Length_in_Air': Coating_1_Wt_per_Unit_Length_in_Air,
                                                     'Contents_Wt_Per_Unit_Length_in_Air':Contents_Wt_Per_Unit_Length_in_Air,
                                                     'Total_Weight_per_Unit_Length_in_Air': Total_Weight_per_Unit_Length_in_Air,
                                                     'Buoyant_Force_per_Unit_Length':Buoyant_Force_per_Unit_Length,
                                                     'Submerged_Weight_per_Unit_Length': Submerged_Weight_per_Unit_Length,
                                                     'Subm_Specific_Gravity_with_respect_to_SW': Subm_Specific_Gravity_with_respect_to_SW
                                                     }
                  )
