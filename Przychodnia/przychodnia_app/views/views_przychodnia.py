from django.shortcuts import render, redirect, reverse
from django.utils import timezone
from django.views.generic.list import ListView
from przychodnia_pacjent.models import Pacjent
from django.shortcuts import get_object_or_404

from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from common.access_decorators_mixins import (
    uprawnienia_wspolne_lekarz_rejestratorka
)
from django.views.generic.detail import DetailView
from przychodnia_wizyta.models import Wizyta
from laboratorium_app.models import BadanieLaboratoryjne
from przychodnia_bad_fiz.models import BadanieFizykalne


@method_decorator(login_required(login_url='/login'), name='dispatch')
@method_decorator(uprawnienia_wspolne_lekarz_rejestratorka, name='dispatch')
class PrzychodniaPacjentLista(ListView):
    template_name = "przychodnia_app/pacjent-lista.html"
    model = Pacjent
    context_object_name = 'pacjenci'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


@method_decorator(login_required(login_url='/login'), name='dispatch')
@method_decorator(uprawnienia_wspolne_lekarz_rejestratorka, name='dispatch')
class PrzychodniaWizytaDetail(DetailView):
    template_name = "przychodnia_app/wizyta-detail.html"
    context_object_name = "wizyta"
    model = Wizyta

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["badania_lab"] = BadanieLaboratoryjne.badania.w_ramach_wizyty(
            wizyta=kwargs.get('object')
        )
        context["badania_fiz"] = BadanieFizykalne.badania.w_ramach_wizyty(
            wizyta=kwargs.get('object')
        )
        return context


@method_decorator(login_required(login_url='/login'), name='dispatch')
@method_decorator(uprawnienia_wspolne_lekarz_rejestratorka, name='dispatch')
class PrzychodniaAnulujWizyte(View):
    template_name = "przychodnia_app/anuluj-wizyte.html"
    def get(self, request, wizyta_id):
        wizyta = get_object_or_404(Wizyta, pk=wizyta_id)
        return render(request, self.template_name, {"wizyta": wizyta})

    def post(self, request, wizyta_id):
        wizyta = get_object_or_404(Wizyta, pk=wizyta_id)
        wizyta.dt_zak_anul = timezone.now()
        wizyta.status = "ANUL"
        wizyta.save()
        return redirect(reverse("common:login"))
