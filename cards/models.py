from django.db import models
import random

class UserProfile(models.Model):
    name = models.CharField(max_length=20)
    age = models.CharField(max_length=20, null=False)
    coin = models.CharField(max_length=20, null=False)
    image = models.ImageField(null=True, blank=True, default='car.png')
    # user_deck = ?

class Card(models.Model):
    
    CLUBS, DIAMONDS, HEARTS, SPADES = 1, 2, 3, 4
    TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, JACK, QUEEN, KING, ACE = 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14

    SUITS = (
    (CLUBS, 'CLUBS'),
    (DIAMONDS, 'DIAMONDS'),
    (HEARTS, 'HEARTS'),
    (SPADES, 'SPADES'),
    )

    NUMBERS = (
    (TWO,'2'),
    (THREE, '3'),
    (FOUR, '4'),
    (FIVE, '5'),
    (SIX, '6'),
    (SEVEN, '7'),
    (EIGHT, '8'),
    (NINE, '9'),
    (TEN, '10'),
    (JACK, 'J'),
    (QUEEN, 'Q'),
    (KING, 'K'),
    (ACE, 'A'),
    )

    suit = models.PositiveSmallIntegerField(choices=SUITS)
    number = models.PositiveSmallIntegerField(choices=NUMBERS)
    image = models.ImageField(null=True, blank=True, default='B-Red.png')

    def __str__(self):
        return f'{self.number} of {self.suit}'


class Deck(models.Model):

    def make_deck():
        card_list = []
        all_cards = Card.objects.all()
        for card in all_cards:
            card =  f'{card.number} of {card.suit}'
            card_list.append(card)
        random.shuffle(card_list)
        a = Deck.deal(card_list)
        return a

    def deal(cards):
        deck_1 = []
        deck_2 = []
        counter = 1

        for i in range(52):
            popped_card = cards.pop(0)

            if counter % 2 == 0:
                deck_1. append(popped_card)
                counter += 1 
            else:
                deck_2. append(popped_card)
                counter += 1 
        return deck_1, deck_2



# check if you win or lose 
    def is_empty(deck_1, deck_2):
        if deck_1 == []:
            return render ("lost.html")

        if deck_2 == []:
            return render ("win.html")
        
# # xxxxxxxxxxxxxxxxxxxxxxxxx

"""
3. create user profile VVVVVVVVVVVVVVVVVVVVVVV

class Card():


    user_deck FK
    def _eq_ equal
    def _gt_ greater then 


class UserDeck()
    user 1 to 1 

    def is empty 
    userdeck1.card_set.all() 

class UserProfile():
    userdeck 1 to 1 
    name 
    age
    coins 
    profile-image



game-logic 
step 1. 
press bet coins 

step 2. 
press start  
to suffle the deck ands devide it between the players
update the data base 
then show the game table 

step 3.
compare decks to see if someone has won the game 

step 4.
press pull
to show the 2 cards 

step 5. 
compare the 2 cards 
if card 1 is bigger then card 2 -- player 1 gets both cards 
if card 2 is bigger then card 1 -- player 2 gets both cards 

is card 1 = card 2 
go back to step 3

"""





"""
from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    class CarType(models.TextChoices):
        CAR = 'C', 'Car'
        TRUCK = 'T', 'Truck'
        MOTORCYCLE = 'M', 'Motorcycle'

    cartype = models.CharField(max_length=3, choices=CarType.choices, default=CarType.CAR)
    number = models.CharField(max_length=20, null=False)
    manufacturer = models.CharField(max_length=20)
    image = models.ImageField(null=True, blank=True,
                              default='car.png')

    def __str__(self):
        typed = self.get_cartype_display()
        return f'{typed} - {self.number}'

class Employee(User):
    class Meta:
        verbose_name = 'Employee'

    tagnumber = models.CharField(max_length=50)

class Treatment(models.Model):
    class TreatmentType(models.IntegerChoices):
        TEN_TOUSAND = 1, '10,000'
        BREAKS = 2, 'BREAKS'
        THIRTY_THOUSAND = 3, '30,000'        
    type = models.IntegerField(choices=TreatmentType.choices, null=False),
    price = models.DecimalField(decimal_places=2, max_digits=10 ,null=False),
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)



"""



''''
junk
    # suit = models.CharField(max_length = 20, null=False, default = SuitType.CLUBS, choices=SuitType.choices)
    # number = models.CharField(max_length = 20, null=False, default = NumberType.TWO, choices=NumberType.choices)
    # suit = models.CharField(max_length=5)
    # number = models.CharField(max_length=5)
    
    # def get_suit_type(self):
    #     for choice in self.SuitType:
    #         if self.type == choice.value:
    #             return choice.label
    #     return 'NO TYPE'

    # def get_number_type(self):
    #     for choice in self.NumberType:
    #         if self.type == choice.value:
    #             return choice.label
    #     return 'NO TYPE'

'''