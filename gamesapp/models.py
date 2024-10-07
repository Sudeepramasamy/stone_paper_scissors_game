from django.db import models

# models.py
from django.db import models

class GameResult(models.Model):
    player_name = models.CharField(max_length=100)
    player_choice = models.CharField(max_length=10)
    computer_choice = models.CharField(max_length=10)
    winner = models.CharField(max_length=10)
    round_number = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.player_name} - Round {self.round_number}: {self.winner}"
