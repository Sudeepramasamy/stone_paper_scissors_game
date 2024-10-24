from django.db import models
from django.utils import timezone

class Player(models.Model):
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class GameResult(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, default=1)
    computer_choice = models.CharField(max_length=10)
    player_choice = models.CharField(max_length=10)
    result = models.CharField(max_length=10) 
    round_number = models.IntegerField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Round {self.round_number} - {self.player.name}: {self.result}"
