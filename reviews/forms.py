from django import forms
from reviews.models import Review


# class Review_form(forms.Form):
#     name = forms.CharField(max_length=20, min_length=3)
#     review = forms.CharField(widget=forms.Textarea, max_length=350, min_length=1)
class Review_form(forms.ModelForm):
    class Meta:
        model = Review   
        fields = ['name', 'review']