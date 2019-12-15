from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from django.contrib.auth import (authenticate, login, logout)


class Login(View):
    template_name = "common/login.html"
    def get(self, request):
        return render(request, self.template_name, {})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        onlogin_msg = "Zalogowano poprawnie jako {who}"
        if user is not None:
            login(request, user)
            # Zdecyduj gdzie przekierować
            if user.is_staff:
                return redirect(reverse('admin:index'))
            if user.role == "REJ":
                messages.success(self.request, onlogin_msg.format(who="Rejestratorka"))
                return redirect(reverse('przychodnia_app:rejestratorka-wizyty-nowe'))
            if user.role == "LEK":
                messages.success(self.request, onlogin_msg.format(who="Lekarz"))
                return redirect(reverse('przychodnia_app:lekarz-moje-wizyty'))
            return redirect("/")
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
