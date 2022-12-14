from django.urls import path
from . import views, game_logic, audio

app_name = 'cards'
urlpatterns = [
    path('', views.main, name="main"),
    # path('game', views.game, name="game"),
    path('win', views.win, name="win"),
    path('lose', views.lose, name="lose"),
    path('betting', views.betting, name="betting"),
    path('show', views.show, name="show"),
    path('leaderboard', views.leaderboard, name="leaderboard"),
    # path('game_round', game_logic.game_round, name="game_round"),
    path('music', audio.music, name="music"),



]
