from django import forms
from cars.models import Brand, Car


class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value is None or value == 0:
            self.add_error('value', 'Value cannot be null or zero.')

    def clean_year(self):
        year = self.cleaned_data.get('year')
        if year is None or year < 2000:
            self.add_error('year', 'Year cannot be less than 2000.')


