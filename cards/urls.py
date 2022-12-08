from django.urls import path
from . import views

app_name = 'cards'
urlpatterns = [
    path('', views.main, name="main"),
    path('game', views.game, name="game"),
    path('win', views.win, name="win"),
    path('lose', views.lose, name="lose"),
    path('betting', views.betting, name="betting")
]
