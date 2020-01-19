from django.urls import path, include

from laboratorium_app import views

app_name = "laboratorium_app"

urlpatterns = [
    ###################################################
    # Laborant
    ###################################################
    path(
        "laborant/",
        views.LaborantDashboard.as_view(),
        name="laborant-dashboard"
    ),
    path(
        "laborant/wykonane-badania",
        views.LaborantWykonaneBadania.as_view(),
        name="laborant-wyk-badania"
    ),
    path(
        "laborant/anulowane-badania",
        views.LaborantAnulowaneBadania.as_view(),
        name="laborant-anul-badania"
    ),
    path(
        "laborant/wykonaj-badanie/<int:pk>/",
        views.LaborantWykAnulView.as_view(),
        name="laborant-wyk-anul"
    ),
    ###################################################
    # Kierownik Laboratorium
    ###################################################
    path(
        "kierownik-laboratorium/",
        views.KierownikLabDashboard.as_view(),
        name="kierownik-lab-dashboard"
    ),
    path(
        "kieronik-laboratorium/zatwierdz-badanie/<int:pk>/",
        views.KierownikZatwAnulView.as_view(),
        name="kierownik-zatw-anul"
    ),
    path(
        "badania-zatwierdzone/",
        views.KierownikZatwierdzoneBadania.as_view(),
        name="laboratorium-bad-lab-zatw-list"
    ),
    ###################################################
    # Badania
    ###################################################
    path(
        "badanie-lab/<int:pk>",
        views.LaboratoriumBadLabDetail.as_view(),
        name="laboratorium-bad-lab-detail"
    ),
]
