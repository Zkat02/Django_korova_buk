from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import BaseWords
from django.views.generic import ListView, CreateView, DetailView

from .forms import UserInputWordForm

from . import game_logic

game = game_logic.Game()


def UserInput(request):
    if request.method == 'POST':
        form = UserInputWordForm(request.POST)

        data = request.POST
        restart = data.get("new_game")

        if restart:
            game.restart()
        else:
            if form.is_valid():
                input_word = form.cleaned_data['word']
                game.User_attempt(input_word)
    else:
        form = UserInputWordForm()
    context = {'form': form} | game.get_context()  # соединение 2х словарей
    return render(request, 'game_app/game.html', context)
