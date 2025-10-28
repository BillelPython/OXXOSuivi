from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Equipes

@login_required(login_url='login')
def liste_equipes(request):
    equipes = Equipes.objects.all()
    return render(request, 'team/liste_equipes.html', {'equipes': equipes})
