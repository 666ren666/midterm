from django.shortcuts import render
from cards.models import Card
from cards.game_logic import deck_2, deck_1
from cards.game_logic import count_cards, draw, greater_than, is_empty


def game(request):

    amount_1 = int(count_cards(deck_1))
    amount_2 = int(count_cards(deck_2))

    a = is_empty(deck_1, deck_2)
    if a == "win":
        return render(request,'win.html')
    if a == "lose":
        return render(request,'lose.html')

    card_1, image_1, value_1 = draw(deck_1)
    card_2, image_2, value_2 = draw(deck_2)

    greater_than(card_1, value_1, deck_1, card_2, value_2, deck_2)

    return render(request,'game.html',{'card_1':image_1, 'card_2':image_2, 'amount_1':amount_1, 'amount_2':amount_2, 'value_1':value_1, 'value_2':value_2})


def main(request):
    return render(request,'main.html')

def win(request):
    return render(request,'win.html')

def lose(request):
    return render(request,'lose.html')

def list(request):
    return render(request,'list.html')

def betting(request):
    return render(request,'betting.html')

def leaderboard(request):
    return render(request,'leader_board.html')


def show(request):

    return render(request,"show.html",{'deck_1':deck_1, 'deck_2':deck_2})






# def game(request):

#     amount_1 = int(count_cards(deck_1))
#     amount_2 = int(count_cards(deck_2))

#     card_1 = deck_1.pop(0)
#     card_string_1 = str(card_1)
#     split_card_1 = card_string_1.split(', ')
#     image_1 = split_card_1[1]
#     value_and_suit_1 = split_card_1[0]
#     split_suit_1 = value_and_suit_1.split(' of')
#     value_1 = int(split_suit_1[0])

#     card_2 = deck_2.pop(0)
#     card_string_2 = str(card_2)
#     split_card_2 = card_string_2.split(', ')
#     image_2 = split_card_2[1]
#     value_and_suit_2 = split_card_2[0]
#     split_suit_2 = value_and_suit_2.split(' of')
#     value_2 = int(split_suit_2[0])

#     greater_than(card_1, card_2, deck_1, deck_2, temp_cards)

#     return render(request,'game.html',{'card_1':image_1, 'card_2':image_2, 'amount_1':amount_1, 'amount_2':amount_2, 'value_1':value_1, 'value_2':value_2})






























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
