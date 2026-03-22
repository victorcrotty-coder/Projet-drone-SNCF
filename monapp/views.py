from datetime import date, timedelta
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils import timezone

from .models import Accueil, Mission, Drone, Station, Donnees, Message


# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    return redirect("login")


@login_required
def dashboard(request):
    # Données pour le dashboard
    current_date = timezone.now().date()

    # Calculer les jours du mois pour le calendrier
    import calendar
    cal = calendar.monthcalendar(current_date.year, current_date.month)
    days_of_month = []
    for week in cal:
        for day in week:
            if day != 0:
                days_of_month.append(day)

    # Récupérer les données
    stations = Station.objects.filter(actif=True)[:10]  # Limiter à 10 pour l'affichage
    missions_today = Mission.objects.filter(
        date_debut__lte=current_date,
        date_fin__gte=current_date
    ) | Mission.objects.filter(
        date_debut=current_date
    )[:5]  # Missions du jour

    recent_alerts = Message.objects.filter(
        type_message='ALERTE',
        created_at__gte=timezone.now() - timedelta(days=1)
    )[:5]  # Alertes récentes

    # Statistiques
    drones_count = Drone.objects.count()
    stations_count = Station.objects.filter(actif=True).count()
    donnees_count = Donnees.objects.count()

    context = {
        'current_date': current_date,
        'days_of_month': days_of_month,
        'stations': stations,
        'missions_today': missions_today,
        'recent_alerts': recent_alerts,
        'drones_count': drones_count,
        'stations_count': stations_count,
        'donnees_count': donnees_count,
    }

    return render(request, "monapp/dashboard.html", context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect("index")

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not email or not password:
            messages.error(request, "Veuillez saisir votre adresse e-mail et votre mot de passe.")
        else:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                user = None

            if user:
                user = authenticate(request, username=user.username, password=password)

            if user is not None:
                login(request, user)
                return redirect("index")

            messages.error(request, "Adresse e-mail ou mot de passe incorrect.")

    return render(request, "monapp/login.html")


@login_required
def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def accueil_list(request):
    accueils = Accueil.objects.filter(actif=True).order_by('-created_at')
    return render(request, "monapp/accueil_list.html", {"accueils": accueils})


@login_required
def mission_list(request):
    missions = Mission.objects.all().order_by('-date_debut', 'statut')
    return render(request, "monapp/mission_list.html", {"missions": missions})


@login_required
def drone_list(request):
    drones = Drone.objects.all().order_by('statut', 'nom')
    return render(request, "monapp/drone_list.html", {"drones": drones})


@login_required
def station_list(request):
    stations = Station.objects.filter(actif=True).order_by('nom')
    return render(request, "monapp/station_list.html", {"stations": stations})


@login_required
def donnees_list(request):
    donnees = Donnees.objects.select_related('station').order_by('-timestamp')
    return render(request, "monapp/donnees_list.html", {"donnees": donnees})


@login_required
def message_list(request):
    messages_obj = Message.objects.all().order_by('-created_at')
    return render(request, "monapp/message_list.html", {"messages": messages_obj})
