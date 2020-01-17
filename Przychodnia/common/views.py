from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from django.contrib.auth import (authenticate, login, logout)


def onlogin_redirect(user, request, onlogin_msg):
    # Zdecyduj gdzie przekierować
    if user.is_staff:
        return redirect(reverse('admin:index'))
    if user.role == "REJ":
        messages.success(request, onlogin_msg.format(who="Rejestratorka"))
        return redirect(reverse('przychodnia_app:rejestratorka-wizyty-nowe'))
    if user.role == "LEK":
        messages.success(request, onlogin_msg.format(who="Lekarz"))
        return redirect(reverse('przychodnia_app:lekarz-moje-wizyty'))
    if user.role == "LAB":
        messages.success(request, onlogin_msg.format(who="Laborant"))
        return redirect(reverse('laboratorium_app:laborant-dashboard'))
    if user.role == "KLAB":
        messages.success(request, onlogin_msg.format(who="Kierownik Laboratorium"))
        return redirect(reverse('laboratorium_app:kierownik-lab-dashboard'))
    return redirect("/")

class Login(View):
    template_name = "common/login.html"
    onlogin_msg = "Zalogowano poprawnie jako {who}"

    def get(self, request):
        # Automatyczne przekierowanie, jesli wyświetla logowanie, a już jest zalogowany
        if request.user.is_authenticated:
            return onlogin_redirect(request.user, self.request, self.onlogin_msg)
        return render(request, self.template_name, {})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Zdecyduj gdzie przekierować
            return onlogin_redirect(user, self.request, self.onlogin_msg)
        else:
            return render(request, self.template_name, {"incorrect": True})


class Logout(View):
    def get(self, request):
        logout(request)
        messages.success(self.request, 'Wylogowano')
        return redirect("common:login")


class RedirectToLoginPage(View):
    def get(self, request):
        return HttpResponseRedirect(reverse("common:login"))
