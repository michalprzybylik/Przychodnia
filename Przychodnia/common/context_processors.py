from django.utils import timezone

from przychodnia_pacjent.models import Pacjent
from przychodnia_wizyta.models import Wizyta
from przychodnia_app.models import (
    Lekarz,
    Rejestratorka
)
from laboratorium_app.models import (
    Laborant,
    KierownikLabarotorium
)

def common_context(request):

    profile = None
    if request.user.is_authenticated:
        if not profile and request.user.role and request.user.role == "REJ":
            profile = Rejestratorka.objects.get(user=request.user)
        if not profile and request.user.role and request.user.role == "LEK":
            profile = Lekarz.objects.get(user=request.user)
        if not profile and request.user.role and request.user.role == "LAB":
            profile = Laborant.objects.get(user=request.user)
        if not profile and request.user.role and request.user.role == "KLAB":
            profile = KierownikLabarotorium.objects.get(user=request.user)

    context = {
        "time_now": timezone.now(),
        "pacjenci_count": Pacjent.objects.count(),
        "nowe_wizyty_count": Wizyta.wizyty.get_new().count(),
        "stare_wizyty_count": Wizyta.wizyty.get_old().count(),
        "profile": profile,
    }
    return context
