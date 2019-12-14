from django.urls import path, include

from przychodnia_app import views

app_name = "przychodnia_app"

urlpatterns = [
    path(
        "rejestratorka/wizyty-nowe",
        views.RejestratorkaWizytyNowe.as_view(),
        name="rejestratorka-wizyty-nowe"
    ),
    path(
        "rejestratorka/wizyty-stare",
        views.RejestratorkaWizytyStare.as_view(),
        name="rejestratorka-wizyty-stare"
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
        "rejestratorka/pacjenci/",
        views.PacjentRejestratorkaList.as_view(),
        name="rejestratorka-pacjenci-list"
    ),
    path(
        "lekarz/",
        views.LekarzDashboard.as_view(),
        name="lekarz-dashboard"
    ),
]
