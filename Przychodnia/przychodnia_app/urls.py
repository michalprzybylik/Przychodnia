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
        "lekarz/",
        views.LekarzDashboard.as_view(),
        name="lekarz-dashboard"
    ),
]
