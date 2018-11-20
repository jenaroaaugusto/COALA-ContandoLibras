from django import forms
from .models import *


class SubscriptionForm(forms.Form):
    class Meta:
        model = SubscriptionsModels
        fields = ('name', 'email', 'telefone', 'message')
