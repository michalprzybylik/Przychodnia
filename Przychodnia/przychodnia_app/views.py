from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.db.models import Q

from przychodnia_app.models import Rejestratorka
from przychodnia_wizyta.models import Wizyta
from przychodnia_pacjent.models import Pacjent

from przychodnia_wizyta.forms import WizytaForm
from przychodnia_pacjent.forms import PacjentForm
from przychodnia_pacjent.forms import AdresForm


class RejestratorkaWizytyNowe(View):
    template_name = "przychodnia_app/rejestratorka-wizyty-nowe.html"
    def get(self, request):
        context = {
            "nowe_wizyty": Wizyta.wizyty.get_new(),
        }
        return render(request, self.template_name, context)


class RejestratorkaWizytyStare(View):
    template_name = "przychodnia_app/rejestratorka-wizyty-stare.html"
    def get(self, request):
        context = {
            "stare_wizyty": Wizyta.wizyty.get_old(),
        }
        return render(request, self.template_name, context)


class LekarzDashboard(View):
    template_name = "przychodnia_app/lekarz-dashboard.html"
    def get(self, request):
        return render(request, self.template_name, {})


class WizytaCreate(CreateView):
    template_name = "przychodnia_app/wizyta-create.html"
    form_class = WizytaForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        rejestratorka = get_object_or_404(Rejestratorka, Q(user__id=self.request.user.id))
        self.object.rejestratorka = rejestratorka
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, 'Wizyta zarejestrowana poprawnie')
        return reverse("przychodnia_app:rejestratorka-wizyty-nowe")


class PacjentCreate(CreateView):
    template_name = "przychodnia_app/pacjent-create.html"
    form_class = PacjentForm

    def get_success_url(self):
        messages.success(self.request, 'Pacjent dodany poprawnie')
        return reverse("przychodnia_app:rejestratorka-rejestruj-wizyte")

class PacjentRejestratorkaList(ListView):
    template_name = "przychodnia_app/pacjent-list-rejestratorka.html"
    model = Pacjent
    context_object_name = 'pacjenci'
    paginate_by = 50

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AdresCreate(CreateView):
    template_name = "przychodnia_app/adres-create.html"
    form_class = AdresForm

    def get_success_url(self):
        messages.success(self.request, 'Adres dodany poprawnie')
        return reverse("przychodnia_app:rejestratorka-dodaj-pacjenta")
