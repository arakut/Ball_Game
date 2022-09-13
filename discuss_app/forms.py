from django import forms

from .models import DiscussText


class DiscussForm(forms.ModelForm):

    class Meta:
        model = DiscussText
        fields = ['text']