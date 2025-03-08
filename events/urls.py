from django.urls import path
from . import views
from .views import participants_par_tranche_age


urlpatterns = [
    path('', views.liste_evenements, name='liste_evenements'),
    path('evenement/<int:event_id>/', views.inscrire_a_evenement, name='inscription_form'),
    path('statistiques/', views.participants_par_tranche_age, name='statistiques'),
]


