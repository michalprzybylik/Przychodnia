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
        if user is not None:
            login(request, user)
            # Zdecyduj gdzie przekierować
            breakpoint()
            if user.role == "REJ":
                return redirect(reverse('przychodnia_app:rejestratorka-dashboard'))
            if user.role == "LEK":
                return redirect(reverse('przychodnia_app:lekarz-dashboard'))
            return redirect("/")
        else:
            return render(request, self.template_name, {"incorrect": True})


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect("/")
