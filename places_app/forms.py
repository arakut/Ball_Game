from django import forms

from .models import Review, Raiting, RaitingPLace


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['text']