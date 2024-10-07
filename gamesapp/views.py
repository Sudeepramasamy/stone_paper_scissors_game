from django.shortcuts import render, redirect
import random
from django.http import JsonResponse
from .models import GameResult
import json
from django.views.decorators.csrf import csrf_exempt

# Home page
def home(request):
    return render(request, 'index.html')

# Play page that gets the player name and renders the game
def play(request):
    if request.method == 'POST':
        playername = request.POST.get('yourname')
        return render(request, 'play.html', {'playername': playername})
    return redirect('home')  # Redirect to home if GET request

@csrf_exempt  # Disable CSRF protection for simplicity, but use CSRF tokens in production
def play_game(request):
    if request.method == "POST":
        data = json.loads(request.body)
        player_choice = data.get("player_choice")
        computer_choice = data.get("computer_choice")
        player_name = data.get("player_name", "Player") 

        # Determine the winner
        result = determine_winner(player_choice, computer_choice, player_name)

        # Send response back to the frontend
        return JsonResponse({"result": result})

def determine_winner(player, computer, player_name):
    # Define game logic
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissor") or \
         (player == "scissor" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return f"{player_name} wins!"
    else:
        return "Computer wins!"