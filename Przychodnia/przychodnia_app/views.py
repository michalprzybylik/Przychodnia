from django.shortcuts import render, redirect
from django.views.generic import View


class RejestratorkaDashboard(View):
    template_name = "przychodnia_app/rejestratorka-dashboard.html"
    def get(self, request):
        return render(request, self.template_name, {})


class LekarzDashboard(View):
    template_name = "przychodnia_app/lekarz-dashboard.html"
    def get(self, request):
        return render(request, self.template_name, {})
