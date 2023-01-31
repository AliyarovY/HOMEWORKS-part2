from django import forms
from django.core.exceptions import ValidationError
from .models import *


class VersionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


    class Meta:
        model = Version
        fields = '__all__'


    def clean_name(self):
        release_notes = self.cleaned_data['release_notes']
        ban = 'казино, криптовалюта, крипта, биржа, дешево, бесплатно, обман, полиция, радар'
        ban = [x.strip() for x in ban.split(',')]
        if release_notes.lower() in ban:
            raise ValidationError('the name is forbidden')
        return release_notes


    def clean_product(self):
        product = self.cleaned_data['product']
        if product not in Product:
            raise ValidationError('incorrect product')
        return prouduct
