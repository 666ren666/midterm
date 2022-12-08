from django.db import models


class UserProfile(models.Model):
    name = models.CharField(max_length=20)
    age = models.CharField(max_length=20, null=False)
    coin = models.CharField(max_length=20, null=False)
    image = models.ImageField(null=True, blank=True, default='car.png')
    # user_deck = ?


class Card(models.Model):

    CLUBS = 0
    DIAMONDS = 1
    HEARTS = 2
    SPADES = 3

    SUITS = (
    (SPADES, 'SPADES'),
    (CLUBS, 'CLUBS'),
    (DIAMONDS, 'DIAMONDS'),
    (HEARTS, 'HEARTS')
    )

    suit = models.PositiveSmallIntegerField(choices=SUITS)
    rank = models.CharField(max_length=5)
    image = models.ImageField(null=True, blank=True, default='B-Red.png')






# def build_cards_to_db(Card):
#     for suit in Card.suit.choices:
#         for number in range(2, 14):
#             card = Card(suit=suit, number=number)




    #         Card.image_connection(suit, number)
    # Card.suit = suit
    # Card.number = number 


# xxxxxxxxxxxxxxxxxxxxxxxxx


# game logic

    def draw(deck_a, deck_b):
        card_a = deck_a.pop(0)
        card_b = deck_b.pop(0)
        return card_a, card_b

    def greater_than(card_a, card_b, deck_a, deck_b):
        Card.draw(deck_a, deck_b)
        if card_a > card_b:
            deck_a.append(card_a, card_b) 
            return deck_a, deck_b
        else:
            deck_b.append(card_a, card_b) 
            return deck_a, deck_b

    def equal(card_a, card_b, deck_a, deck_b):
        temp_cards = []
        Card.draw(deck_a, deck_b)
        if card_a == card_b:
            temp_cards.append(card_a, card_b)
            Card.draw()
            Card.greater_than()





# class User_Deck(models.Model):
#     def is_empty(deck)
#         if deck == []
#         return render ("lost.html")
        
# # xxxxxxxxxxxxxxxxxxxxxxxxx


#     def shuffle(self):
#         for i in range(len(self.cards)-1, 0, -1):
#             r = random.randint(0, i)
#             self.cards[i], self.cards[r] = self.cards[r], self.cards[i]



"""
3. create user profile VVVVVVVVVVVVVVVVVVVVVVV




2. create card building function (init) 

class Card():
    suit   -> e-num
    number -> e-num
    image
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