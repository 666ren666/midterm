from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request,'main.html')

def win(request):
    return render(request,'win.html')

def lose(request):
    return render(request,'lose.html')

def game(request):
    return render(request,'game.html')

def list(request):
    return render(request,'list.html')





""""
from django.shortcuts import render, redirect
from django.contrib import messages 
from .models import Car, Employee, Treatment
# Create your views here.
from .forms import TreatmentForm

def cars(request):
    cars = Car.objects.all()
    return render(request,'cars.html', {'cars':cars})

def treatment(request):
    form = TreatmentForm()
    # cars = Car.objects.all()
    # employees = Employee.objects.all()
    context = { 
            'form': form
            }
    if request.method == "GET":
        return render(request,"treatment.html",context=context)
    else:
        form = TreatmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Saved Succesfuly!")
            redirect('cars')
    
        return render(request,"treatment.html",{'form':form})

def treatments(request):
        treatments = Treatment.objects.all()
        return render(request,"treatments.html",{'treatments':treatments})

def charts(request):

        ten = Treatment.objects.filter(type=Treatment.TreatmentType.TEN_TOUSAND).count()
        breaks = Treatment.objects.filter(type=Treatment.TreatmentType.BREAKS).count()
        thirty = Treatment.objects.filter(type=Treatment.TreatmentType.THIRTY_THOUSAND).count()

        return render(request,"charts.html",{'ten':ten, 'breaks':breaks, 'thirty':thirty })
        
            
        



"""