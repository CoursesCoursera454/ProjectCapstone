#importing modules
from rest_framework.serializers import ModelSerializer
from .models import Menu, Booking

#create menu serializer
class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

#booking serilizer
class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'