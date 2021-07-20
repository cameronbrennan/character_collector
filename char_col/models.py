from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.
CAMPAIGNS = (
    ('S', 'Scheduled'),
    ('P', 'In Progress'),
    ('C', 'Completed'),
)

class Ability(models.Model):
    abil_name = models.CharField(max_length=50)
    abil_type = models.CharField(max_length=50)
    abil_damage = models.CharField(max_length=50)

    def __str__(self):
        return self.abil_name
    def get_absolute_url(self):
        return reverse('ability_detail', kwargs={'pk': self.id})

class Character(models.Model):
    char_name = models.CharField(max_length=50)
    char_class = models.CharField(max_length=50)
    char_race = models.CharField(max_length=50)
    abilities = models.ManyToManyField(Ability)

    def __str__(self):
        return self.char_name

class Campaign(models.Model):
    date = models.DateField('campaign date')
    status = models.CharField(
        max_length=1,
        choices=CAMPAIGNS,
        default=CAMPAIGNS[0][0]
    )
    character = models.ForeignKey(Character, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_campaign_status()} on {self.date}"
    class Meta:
        ordering = ['-date']