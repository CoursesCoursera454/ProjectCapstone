#importing modules
from django.forms import ModelForm
from .models import Booking

#creating class
class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

