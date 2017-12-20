from django import forms


class CreateReview(forms.Form):
    message = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': '3'}))
    rating = forms.IntegerField(max_value=10, min_value=0)
