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
    ###################################################
    # Lekarz
    ###################################################
    path(
        "lekarz/moje-wizyty",
        views.LekarzDashboard.as_view(),
        name="lekarz-moje-wizyty"
    ),
    path(
        "lekarz/moje-zakonczone-wizyty",
        views.LekarzZakonczoneWizyty.as_view(),
        name="lekarz-moje-zakonczone-wizyty"
    ),
    ###################################################
    # Wspólne (przychodnia)
    ###################################################
    path(
        "anuluj-wizyte/<int:wizyta_id>/",
        views.PrzychodniaAnulujWizyte.as_view(),
        name="przychodnia-anuluj-wizyte"
    ),
    path(
        "pacjenci/",
        views.PrzychodniaPacjentLista.as_view(),
        name="przychodnia-pacjenci-list"
    ),
    path(
        "wizyta/<int:pk>/",
        views.PrzychodniaWizytaDetail.as_view(),
        name="przychodnia-wizyta-detail"
    ),
]
