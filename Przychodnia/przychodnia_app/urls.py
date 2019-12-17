from django.urls import path, include

from przychodnia_app import views

app_name = "przychodnia_app"

urlpatterns = [
    ###################################################
    # Rejestratorka
    ###################################################
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
        views.RejestratorkaWizytaDodaj.as_view(),
        name="rejestratorka-rejestruj-wizyte"
    ),
    path(
        "rejestratorka/dodaj-pacjenta/",
        views.RejestratorkaPacjentDodaj.as_view(),
        name="rejestratorka-dodaj-pacjenta"
    ),
    path(
        "rejestratorka/dodaj-adres/",
        views.RejestratorkaAdresDodaj.as_view(),
        name="rejestratorka-dodaj-adres"
    ),
    path(
        "rejestratorka/anuluj-wizyte/<int:wizyta_id>/",
        views.RejestratorkaAnulujWizyte.as_view(),
        name="rejestratorka-anuluj-wizyte"
    ),
    ###################################################
    # Lekarz
    ###################################################
    path(
        "lekarz/moje-wizyty",
        views.LekarzDashboard.as_view(),
        name="lekarz-moje-wizyty"
    ),
    ###################################################
    # Wspólne
    ###################################################
    path(
        "rejestratorka/pacjenci/",
        views.PacjentLista.as_view(),
        name="pacjenci-list"
    ),
    path(
        "rejestratorka/wizyta/<int:pk>/",
        views.RejestratorkaWizytaDetail.as_view(),
        name="wizyta-detail"
    ),
]
