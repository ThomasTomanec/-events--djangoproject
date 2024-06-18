from django import forms
from .models import SportEvent, MemberClient

class SportEventForm(forms.ModelForm):
    class Meta:
        model = SportEvent
        fields = ['name', 'location', 'result', 'client']

class MemberClientForm(forms.ModelForm):
    class Meta:
        model = MemberClient
        fields = ['first_name', 'last_name', 'email', 'photo']  # Přidáno 'photo'
        widgets = {
            'photo': forms.FileInput(attrs={'class': 'form-control-file'})  # Widget pro nahrání souboru
        }