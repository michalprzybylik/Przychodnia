from django import forms

from przychodnia_pacjent.models import Pacjent
from przychodnia_wizyta.models import Wizyta

class WizytaForm(forms.ModelForm):
    class Meta:
        model = Wizyta
        fields = ("pacjent", "lekarz", "dt_rej") # opis

    def __init__(self, *args, **kwargs):
        super(WizytaForm, self).__init__(*args, **kwargs)
        # self.fields['opis'].widget.attrs.update({'class': 'form-control'})
        self.fields['pacjent'].widget.attrs.update({
            'class': 'form-control select2-select'
        })
        self.fields['lekarz'].widget.attrs.update({
            'class': 'form-control select2-select'
        })
        self.fields['dt_rej'].widget.attrs.update({
            'id': 'datepicker_dt_rej',
            'autocomplete': 'off',
        })
