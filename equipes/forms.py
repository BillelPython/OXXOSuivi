from django import forms

from team.models import Equipes
from .models import Equipes , Evaluation ,Affectation

class EquipeForm(forms.ModelForm):
    class Meta:
        model = Equipes
        fields = ['franchise','nom', 'chef_equipe', 'nombre_poseurs', 'telephone']


class EvaluationForm(forms.ModelForm):
    class Meta:
        model = Evaluation
        fields = ['affectation', 'ponctualite', 'qualite_travail', 'respect_client', 'commentaire']
        widgets = {
            'affectation': forms.Select(attrs={'class': 'form-select'}),
            'ponctualite': forms.Select(attrs={'class': 'form-select'}),
            'qualite_travail': forms.Select(attrs={'class': 'form-select'}),
            'respect_client': forms.Select(attrs={'class': 'form-select'}),
            'commentaire': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class AffectationForm(forms.ModelForm):
    class Meta:
        model = Affectation
        fields = ['franchise', 'equipes', 'commande', 'nombre_menuiseries', 'date_affectation']
        widgets = {
            'franchise': forms.Select(attrs={'class': 'form-control'}),
            'equipes': forms.Select(attrs={'class': 'form-control'}),
            'commande': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'N° commande'}),
            'nombre_menuiseries': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'date_affectation': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

