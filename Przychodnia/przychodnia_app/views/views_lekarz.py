from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.db.models import Q

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from common.access_decorators_mixins import uprawniania_lekarz_wymagane

from przychodnia_wizyta.models import Wizyta
from przychodnia_app.models import Lekarz


def lekarz_by_request(request):
    return Lekarz.objects.get(user=request.user)


@method_decorator(login_required(login_url='/login'), name='dispatch')
@method_decorator(uprawniania_lekarz_wymagane, name='dispatch')
class LekarzDashboard(View):
    template_name = "przychodnia_app/lekarz/moje-wizyty.html"
    def get(self, request):
        ja = lekarz_by_request(request)
        moje_wizyty = Wizyta.wizyty.filter_by_lekarz(ja, typ="REJ")
        moje_wizyty_count = moje_wizyty.count()
        return render(request, self.template_name, {
            "moje_wizyty": moje_wizyty,
            "moje_wizyty_count": moje_wizyty_count,
        })


@method_decorator(login_required(login_url='/login'), name='dispatch')
@method_decorator(uprawniania_lekarz_wymagane, name='dispatch')
class LekarzZakonczoneWizyty(View):
    template_name = "przychodnia_app/lekarz/moje-zakonczone-wizyty.html"
    def get(self, request):
        ja = lekarz_by_request(request)
        zakonczone_wizyty = Wizyta.wizyty.filter_by_lekarz(ja, typ="ZAK")
        return render(request, self.template_name, {
            "zakonczone_wizyty": zakonczone_wizyty
        })
