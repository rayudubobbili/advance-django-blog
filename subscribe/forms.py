from django.forms import ModelForm
from .models import Subscribers


class Subscriber_form(ModelForm):

    class Meta:
        model = Subscribers
        fields = ['name', 'email']

    def clear(self):
        cleaned_data = super(Subscriber_form, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
