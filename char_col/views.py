from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Character, Ability, Campaign
from .forms import CampaignForm


# Create your views here.
def home(request):
    return render(request, 'home.html')

def characters_index(request):
    characters = Character.objects.all()
    return render(request, 'characters/index.html', { 'characters': characters })

def character_detail(request, character_id):
    character = Character.objects.get(id=character_id)
    ability_char_doesnt_have = Ability.objects.exclude(id__in = character.abilities.all().values_list('id'))
    campaign_form = CampaignForm()
    return render(request, 'characters/detail.html', {
        'character': character,
        'campaign_form': campaign_form,
        'abilities': ability_char_doesnt_have
    })

class CharacterCreate(CreateView):
    model = Character
    fields = ['char_name', 'char_class', 'char_race']
    success_url = '/'

class CharacterUpdate(UpdateView):
    model = Character
    fields = ['char_name', 'char_class', 'char_race']
    success_url = '/'

class CharacterDelete(DeleteView):
    model = Character
    fields = ['char_name', 'char_class', 'char_race']
    success_url = '/'

def add_ability(request, character_id, ability_id):
    Character.objects.get(id=character_id).abilities.add(ability_id)
    return redirect('detail', character_id=character_id)

def remove_ability(request, character_id, ability_id):
    Character.objects.get(id=character_id).abilities.remove(ability_id)
    return redirect('detail', character_id=character_id)

class AbilityCreate(CreateView):
    model = Ability
    fields = '__all__'

class AbilityUpdate(UpdateView):
    model = Ability
    fields = ['abil_type', 'abil_damage']
    success_url = '/abilities/'

class AbilityList(ListView):
    model = Ability
    fields = '__all__'

class AbilityDetail(DetailView):
    model = Ability
    fields = '__all__'

class AbilityDelete(DeleteView):
    model = Ability
    success_url = '/abilities/'

def add_campaign(request, character_id):
    form = CampaignForm(request.POST)
    if form.is_valid():
        new_campaign = form.save(commit=False)
        new_campaign.character_id = character_id
        new_campaign.save()
    return redirect('detail', character_id=character_id)