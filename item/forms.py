
from django import forms
from .models import Reservation, Cars
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class ReservationForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = ['car','start_date', 'end_date']
        car= forms.ChoiceField

    start_date = forms.DateField(widget=forms.TextInput(attrs={
         'type': 'date' , 'class':'w-full py-4 px-6 rounded-xl'
    }))

    end_date = forms.DateField(widget=forms.TextInput(attrs={
         'type': 'date' , 'class':'w-full py-4 px-6 rounded-xl'
    }))

    def clean(self):
        cleaned_data = super().clean()
        car = cleaned_data.get('car')
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
       

        if car and start_date and end_date:
    
            reservations = Reservation.objects.filter(car=car, end_date__gt=start_date, start_date__lt=end_date)
            if reservations.exists():
                 raise ValidationError('The car is already reserved for the selected dates. Please choose another reservation date.')
         
                
