from django.forms import ModelForm
from app.models import Custormer

class CustomerForm(ModelForm):
    
    class Meta:
        model = Custormer
        fields = '__all__'
