from django.db import models


class UserProfile(models.Model):
    name = models.CharField(max_length=20)
    age = models.CharField(max_length=20, null=False)
    coin = models.IntegerField(null=False, default='1000')
    image = models.ImageField(null=True, blank=True, default='car.png')
    # user_deck = ?

    def __str__(self):
        return f'{self.name} has {self.coin} coins'

class Card(models.Model):
    CLUBS, DIAMONDS, HEARTS, SPADES = 1, 2, 3, 4
    TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, JACK, QUEEN, KING, ACE = 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14

    SUITS = ((CLUBS, 'CLUBS'), (DIAMONDS, 'DIAMONDS'), (HEARTS, 'HEARTS'), (SPADES, 'SPADES'),)
    NUMBERS = ((TWO,'2'),(THREE, '3'),(FOUR, '4'),(FIVE, '5'),(SIX, '6'),(SEVEN, '7'),(EIGHT, '8'),(NINE, '9'),(TEN, '10'),(JACK, 'J'),(QUEEN, 'Q'),(KING, 'K'),(ACE, 'A'),)

    suit = models.PositiveSmallIntegerField(choices=SUITS)
    number = models.PositiveSmallIntegerField(choices=NUMBERS)
    image = models.ImageField(null=True, blank=True, default='B-Red.png')

    def __str__(self):
        typed_suit = self.get_suit_display()
        typed_number = self.get_number_display()
        return f'{typed_number} of {typed_suit}'

class Deck(models.Model):
    deck_name = models.CharField(max_length=100,default="deck_player_name")
    amount_of_cards = models.IntegerField(null=False, default=52)
    user_profile = models.OneToOneField(UserProfile, on_delete = models.CASCADE, primary_key = True, default ="user_1" )
    
    def __str__(self):
        return f'{self.deck_name} has {self.amount_of_cards} cards in his/her deck'



# game-logic 
# step 1. 
# press bet coins 

# step 2. 
# press start  
# to suffle the deck ands devide it between the players
# update the data base 
# then show the game table 

# step 3.
# compare decks to see if someone has won the game 

# step 4.
# press pull
# to show the 2 cards 

# step 5. 
# compare the 2 cards 
# if card 1 is bigger then card 2 -- player 1 gets both cards 
# if card 2 is bigger then card 1 -- player 2 gets both cards 

# is card 1 = card 2 
# go back to step 3


# class Car(models.Model):
#     class CarType(models.TextChoices):
#         CAR = 'C', 'Car'
#         TRUCK = 'T', 'Truck'
#         MOTORCYCLE = 'M', 'Motorcycle'

#     cartype = models.CharField(max_length=3, choices=CarType.choices, default=CarType.CAR)
#     number = models.CharField(max_length=20, null=False)
#     manufacturer = models.CharField(max_length=20)
#     image = models.ImageField(null=True, blank=True, default='car.png')

#     def __str__(self):
#         typed = self.get_cartype_display()
#         return f'{typed} - {self.number}'

# class Employee(User):
#     class Meta:
#         verbose_name = 'Employee'

#     tagnumber = models.CharField(max_length=50)

# class Treatment(models.Model):
#     class TreatmentType(models.IntegerChoices):
#         TEN_TOUSAND = 1, '10,000'
#         BREAKS = 2, 'BREAKS'
#         THIRTY_THOUSAND = 3, '30,000'        
#     type = models.IntegerField(choices=TreatmentType.choices, null=False),
#     price = models.DecimalField(decimal_places=2, max_digits=10 ,null=False),
#     employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
#     car = models.ForeignKey(Car, on_delete=models.CASCADE)


#     # suit = models.CharField(max_length = 20, null=False, default = SuitType.CLUBS, choices=SuitType.choices)
#     # number = models.CharField(max_length = 20, null=False, default = NumberType.TWO, choices=NumberType.choices)
#     # suit = models.CharField(max_length=5)
#     # number = models.CharField(max_length=5)
    

#     # def get_number_type(self):
#     #     for choice in self.NumberType:
#     #         if self.type == choice.value:
#     #             return choice.label
#     #     return 'NO TYPE'


# def get_suit_type(self):
#     for choice in self.SuitType:
#         if self.suit == choice.value:
#             return choice.label
#     return 'NO TYPE'



