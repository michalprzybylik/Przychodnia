from django import forms

from przychodnia_wizyta.models import Wizyta

class WizytaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(WizytaForm, self).__init__(*args, **kwargs)
        self.fields['opis'].widget.attrs.update({'class': 'form-control'})
        self.fields['pacjent'].widget.attrs.update({
            'class': 'form-control select2-select'
        })
        self.fields['lekarz'].widget.attrs.update({
            'class': 'form-control select2-select'
        })

    class Meta:
        model = Wizyta
        fields = ("opis", "pacjent", "lekarz")
