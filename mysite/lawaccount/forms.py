from lawaccount.models import Client, ServiceLog
from django.forms import ModelForm

class ClientForm(ModelForm):
    class Meta:
        model = Client