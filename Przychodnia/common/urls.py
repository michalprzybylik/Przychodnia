from django.urls import path, include

from common import views

app_name = "common"

urlpatterns = [
    path(
        "login/",
        views.Login.as_view(),
        name="login"
    ),
    path(
        "logout/",
        views.Logout.as_view(),
        name="logout"
    ),
    path(
        "",
        views.RedirectToLoginPage.as_view(),
        name="homepage"
    ),
]
