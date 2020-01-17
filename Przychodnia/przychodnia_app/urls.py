from django.urls import path, include

from przychodnia_app import views
from przychodnia_bad_fiz import views as bad_fiz_views
from przychodnia_pacjent import views as pacjent_views

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
    path(
        "lekarz/moje-anulowane-wizyty",
        views.LekarzAnulowaneWizyty.as_view(),
        name="lekarz-moje-anulowane-wizyty"
    ),
    path(
        "lekarz/wizyta/<int:wizyta_id>/realizuj/",
        views.LekarzRealizujWizyte.as_view(),
        name="lekarz-realizuj-wizyte"
    ),
    path(
        "lekarz/wizyta/<int:wizyta_id>/realizuj/inne-wizyty-pacjenta",
        views.LekarzPrzegladajInneWizyty.as_view(),
        name="przegladaj-inne-wizyty-pacjenta"
    ),
    path(
        "lekarz/wizyta/<int:wizyta_id>/realizuj/zlec-badanie-lab/",
        views.LekarzZlecBadanieLaboratoryjne.as_view(),
        name="lekarz-zlec-badanie-lab"
    ),
    path(
        "lekarz/wizyta/<int:wizyta_id>/realizuj/wykonaj-badanie-fiz/",
        views.LekarzWykonajBadanieFizykalne.as_view(),
        name="lekarz-wykonaj-badanie-fiz"
    ),
    ###################################################
    # Lekarz (Bad Fiz)
    ###################################################
    path(
        "lekarz/badanie-fiz/<int:pk>",
        bad_fiz_views.PrzychodniaBadFizDetail.as_view(),
        name="lekarz-bad-fiz-detail"
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
        "pacjent/<int:pk>/",
        pacjent_views.PacjentDetailView.as_view(),
        name="przychodnia-pacjent-detail"
    ),
    path(
        "pacjent/<int:pk>/badania",
        pacjent_views.PacjentBadaniaView.as_view(),
        name="przychodnia-pacjent-badania"
    ),
    path(
        "wizyta/<int:pk>/",
        views.PrzychodniaWizytaDetail.as_view(),
        name="przychodnia-wizyta-detail"
    ),
]
