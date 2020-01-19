from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.generic.list import ListView
from django.utils import timezone
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from common.access_decorators_mixins import (
    uprawniania_laborant_wymagane,
    uprawniania_kierownik_lab_wymagane,
    uprawniania_przegladanie_badan_wymagane
)
from laboratorium_app.models import BadanieLaboratoryjne, Laborant, KierownikLabarotorium
from django.views.generic import View
from laboratorium_app.forms import BadanieLabWykonaj


def laborant_by_request(request):
    return Laborant.objects.get(user=request.user)

def kier_lab_by_request(request):
    return KierownikLabarotorium.objects.get(user=request.user)


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
        context = {}
        context["badania"] = BadanieLaboratoryjne.badania.filter(status="ZLE")
        return render(request, self.template_name, context)


@method_decorator(login_required(login_url='/login'), name='dispatch')
@method_decorator(uprawniania_kierownik_lab_wymagane, name='dispatch')
class KierownikLabDashboard(View):
    template_name = "laboratorium_app/kierownik-lab-dashboard.html"
    def get(self, request):
        return render(request, self.template_name, {})


@method_decorator(login_required(login_url='/login'), name='dispatch')
@method_decorator(uprawniania_przegladanie_badan_wymagane, name='dispatch')
class LaborantWykonaneBadania(ListView):
    template_name = "laboratorium_app/laborant-wyk-badania.html"
    paginate_by = 20
    model = BadanieLaboratoryjne
    context_object_name = "wyk_badania"
    allow_empty = True

    def get_queryset(self):
        return self.model.badania.filter(status="WYK")

@method_decorator(login_required(login_url='/login'), name='dispatch')
@method_decorator(uprawniania_przegladanie_badan_wymagane, name='dispatch')
class LaborantAnulowaneBadania(ListView):
    template_name = "laboratorium_app/laborant-anul-badania.html"
    paginate_by = 20
    model = BadanieLaboratoryjne
    context_object_name = "anul_badania"
    allow_empty = True

    def get_queryset(self):
        return self.model.badania.filter(
            Q(status="ANUL_LAB") | Q(status="ANUL_KLAB")
        )


@method_decorator(login_required(login_url='/login'), name='dispatch')
@method_decorator(uprawniania_laborant_wymagane, name='dispatch')
class LaborantWykAnulView(DetailView):
    template_name = "laboratorium_app/laborant-wyk-anul.html"
    context_object_name = "badania"
    model = BadanieLaboratoryjne

    def post(self, request, **kwargs):
        ja = laborant_by_request(request)
        badanie = get_object_or_404(BadanieLaboratoryjne, id=kwargs.get("pk"))
        wynik = request.POST.get("wynik")
        bad_wyk_action = request.POST.get("bad_wyk_action")
        bad_anul_action = request.POST.get("bad_anul_action")

        if bad_wyk_action:
            messages.success(self.request, "Wykonano badanie laboratoryjne")
            badanie.wynik = wynik
            badanie.status = "WYK"
            badanie.dt_wyk_anul_lab = timezone.now()
            badanie.laborant = ja
            badanie.save()

        if bad_anul_action:
            messages.success(self.request, "Anulowano badanie laboratoryjne")
            badanie.wynik = wynik
            badanie.status = "ANUL_LAB"
            badanie.dt_wyk_anul_lab = timezone.now()
            badanie.laborant = ja
            badanie.save()

        return redirect(reverse("laboratorium_app:laborant-dashboard"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = BadanieLabWykonaj(instance=kwargs.get("object"))
        return context
