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
    ###################################################
    # Kierownik Laboratorium
    ###################################################
    path(
        "kierownik-laboratorium/",
        views.KierownikLabDashboard.as_view(),
        name="kierownik-lab-dashboard"
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
