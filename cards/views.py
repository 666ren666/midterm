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
