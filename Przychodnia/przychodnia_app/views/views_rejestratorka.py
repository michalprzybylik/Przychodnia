from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
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

from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from common.access_decorators_mixins import uprawniania_rejestratorka_wymagane


@method_decorator(login_required(login_url='/login'), name='dispatch')
@method_decorator(uprawniania_rejestratorka_wymagane, name='dispatch')
class RejestratorkaWizytyNowe(View):
    template_name = "przychodnia_app/rejestratorka/wizyty-nowe.html"
    def get(self, request):
        context = {
            "nowe_wizyty": Wizyta.wizyty.get_new(),
        }
        return render(request, self.template_name, context)


@method_decorator(login_required(login_url='/login'), name='dispatch')
@method_decorator(uprawniania_rejestratorka_wymagane, name='dispatch')
class RejestratorkaWizytyStare(View):
    template_name = "przychodnia_app/rejestratorka/wizyty-stare.html"
    def get(self, request):
        context = {
            "stare_wizyty": Wizyta.wizyty.get_old(),
        }
        return render(request, self.template_name, context)


@method_decorator(login_required(login_url='/login'), name='dispatch')
@method_decorator(uprawniania_rejestratorka_wymagane, name='dispatch')
class RejestratorkaWizytaDodaj(CreateView):
    template_name = "przychodnia_app/rejestratorka/wizyta-dodaj.html"
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


@method_decorator(login_required(login_url='/login'), name='dispatch')
@method_decorator(uprawniania_rejestratorka_wymagane, name='dispatch')
class RejestratorkaPacjentDodaj(CreateView):
    template_name = "przychodnia_app/rejestratorka/pacjent-dodaj.html"
    form_class = PacjentForm

    def get_success_url(self):
        messages.success(self.request, 'Pacjent dodany poprawnie')
        return reverse("przychodnia_app:rejestratorka-rejestruj-wizyte")



@method_decorator(login_required(login_url='/login'), name='dispatch')
@method_decorator(uprawniania_rejestratorka_wymagane, name='dispatch')
class RejestratorkaAdresDodaj(CreateView):
    template_name = "przychodnia_app/rejestratorka/adres-dodaj.html"
    form_class = AdresForm

    def get_success_url(self):
        messages.success(self.request, 'Adres dodany poprawnie')
        return reverse("przychodnia_app:rejestratorka-dodaj-pacjenta")


class RejestratorkaAnulujWizyte(View):
    template_name = "przychodnia_app/rejestratorka/anuluj-wizyte.html"
    def get(self, request, wizyta_id):
        wizyta = get_object_or_404(Wizyta, pk=wizyta_id)
        return render(request, self.template_name, {"wizyta": wizyta})

    def post(self, request, wizyta_id):
        wizyta = get_object_or_404(Wizyta, pk=wizyta_id)
        wizyta.dt_zak_anul = timezone.now()
        wizyta.status = "ANUL"
        wizyta.save()
        return redirect(reverse("przychodnia_app:rejestratorka-wizyty-stare"))
