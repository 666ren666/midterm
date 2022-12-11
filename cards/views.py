from django.shortcuts import render
from cards.models import Card
from cards.utils import make_deck 
from cards.game_logic import draw
# Create your views here.

def main(request):
    return render(request,'main.html')

def win(request):
    return render(request,'win.html')

def lose(request):
    return render(request,'lose.html')

def game(request):

    both_decks = make_deck()
    deck_1 = (both_decks[0])
    deck_2 = (both_decks[1])

    card_1 = draw(deck_1)
    card_string = str(card_1)
    split_card = card_string.split(', ')
    image_1 = split_card[1]
    
    card_2 = draw(deck_2)
    card_string = str(card_2)
    split_card = card_string.split(', ')
    image_2 = split_card[1]

    return render(request,'game.html',{'card_1':image_1, 'card_2':image_2 } )

def list(request):
    return render(request,'list.html')

def betting(request):
    return render(request,'betting.html')


def show(request):
    deck_1=[]
    deck_2=[]
    both_decks = make_deck()
    deck_1.append(both_decks[0])
    deck_2.append(both_decks[1])

    return render(request,"show.html",{'deck_1':deck_1, 'deck_2':deck_2})






























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
        
            
        

    # card = str(card_1)
    # card_split_to_list = card.split(",")
    # my_image = card_split_to_list(1) 


"""
