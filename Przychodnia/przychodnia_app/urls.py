from django.urls import path, include

from przychodnia_app import views

app_name = "przychodnia_app"

urlpatterns = [
    path(
        "rejestratorka/",
        views.RejestratorkaDashboard.as_view(),
        name="rejestratorka-dashboard"
    ),
    path(
        "rejestratorka/rejestruj-wizyte/",
        views.WizytaCreate.as_view(),
        name="rejestratorka-rejestruj-wizyte"
    ),
    path(
        "rejestratorka/dodaj-pacjenta/",
        views.PacjentCreate.as_view(),
        name="rejestratorka-dodaj-pacjenta"
    ),
    path(
        "rejestratorka/dodaj-adres/",
        views.AdresCreate.as_view(),
        name="rejestratorka-dodaj-adres"
    ),
    path(
        "lekarz/",
        views.LekarzDashboard.as_view(),
        name="lekarz-dashboard"
    ),
]
