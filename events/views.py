from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Event, Inscription
from .forms import InscriptionForm
from django.shortcuts import render
from django.db.models import Count, Case, When, Value
from .models import Inscription, Accompagnant
from django.db import models
from django.http import HttpResponse
from django.utils import timezone
import pytz


def liste_evenements(request):
    events = Event.objects.all()
    return render(request, 'events/liste_evenements.html', {'events': events})

def inscrire_a_evenement(request, event_id):
    event = get_object_or_404(Event, pk=event_id)

    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            inscription = form.save(commit=False)
            inscription.event = event
            inscription.save()
            messages.success(request, 'Inscription réussie !')
            return redirect('liste_evenements')
    else:
        form = InscriptionForm()

    return render(request, 'events/inscription_form.html', {'form': form, 'event': event})




def participants_par_tranche_age(request):
    # Définition des tranches d'âge
    tranches = {
        "0-18 ans": (0, 18),
        "18-30 ans": (18, 30),
        "30-50 ans": (30, 50),
        "50-65 ans": (50, 65),
        "65 ans et +": (65, 200)
    }
    # Initialisation du comptage
    stats = {tranche: 0 for tranche in tranches}
    # Inclure les participants principaux
    for inscription in Inscription.objects.all():
        # Age du participant principal
        age_principal = inscription.age
        if age_principal is not None:
            for tranche, (min_age, max_age) in tranches.items():
                if min_age <= age_principal < max_age:
                    stats[tranche] += 1
                    break  # Dès qu'on trouve la bonne tranche, on arrête
     # Récupérer les âges des accompagnants
    for accompagnant in Accompagnant.objects.all():
        age = accompagnant.age
        for tranche, (min_age, max_age) in tranches.items():
            if min_age <= age < max_age:
                stats[tranche] += 1
                break  # Dès qu'on trouve la bonne tranche, on arrête

    return render(request, 'events/statistiques.html', {'stats': stats})



def set_user_timezone(request):
    user_timezone = request.GET.get('timezone', 'Europe/Paris')  # Détection par défaut
    timezone.activate(pytz.timezone(user_timezone))
    return HttpResponse(f"Fuseau horaire activé : {user_timezone}")
