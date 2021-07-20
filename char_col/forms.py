from django.forms import ModelForm
from .models import Campaign

class CampaignForm(ModelForm):
    class Meta:
        model = Campaign
        fields = ['date', 'status']