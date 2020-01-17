from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from common.access_decorators_mixins import (
    uprawniania_laborant_wymagane,
    uprawniania_kierownik_lab_wymagane,
    uprawniania_przegladanie_badan_wymagane
)
from laboratorium_app.models import BadanieLaboratoryjne
from django.views.generic import View

# Create your views here.
@method_decorator(login_required(login_url='/login'), name='dispatch')
@method_decorator(uprawniania_przegladanie_badan_wymagane, name='dispatch')
class LaboratoriumBadLabDetail(DetailView):
    template_name = "laboratorium_app/bad-lab-detail.html"
    context_object_name = "badanie_lab"
    model = BadanieLaboratoryjne

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


@method_decorator(login_required(login_url='/login'), name='dispatch')
@method_decorator(uprawniania_laborant_wymagane, name='dispatch')
class LaborantDashboard(View):
    template_name = "laboratorium_app/laborant-dashboard.html"
    def get(self, request):
        # ja = lekarz_by_request(request)
        # moje_wizyty = Wizyta.wizyty.filter_by_lekarz(ja, typ="REJ")
        # moje_wizyty_count = moje_wizyty.count()
        return render(request, self.template_name, {})


@method_decorator(login_required(login_url='/login'), name='dispatch')
@method_decorator(uprawniania_kierownik_lab_wymagane, name='dispatch')
class KierownikLabDashboard(View):
    template_name = "laboratorium_app/kierownik-lab-dashboard.html"
    def get(self, request):
        # ja = lekarz_by_request(request)
        # moje_wizyty = Wizyta.wizyty.filter_by_lekarz(ja, typ="REJ")
        # moje_wizyty_count = moje_wizyty.count()
        return render(request, self.template_name, {})
