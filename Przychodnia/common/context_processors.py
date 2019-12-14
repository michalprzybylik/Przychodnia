from django.utils import timezone

from przychodnia_pacjent.models import Pacjent
from przychodnia_wizyta.models import Wizyta

def common_context(request):
    context = {
        "time_now": timezone.now(),
        "pacjenci_count": Pacjent.objects.count(),
        "nowe_wizyty_count": Wizyta.wizyty.get_new().count(),
        "stare_wizyty_count": Wizyta.wizyty.get_old().count(),
    }
    return context
