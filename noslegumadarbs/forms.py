from django import forms

from noslegumadarbs.deposits.models import Deposit


class Deposit(forms.ModelForm):
    class Meta:
        model = Deposit
        fields = [
            'deposit',
            'term',
            'rate',
        ]
