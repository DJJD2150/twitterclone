from django import forms

# Create your forms here.
class TweetForm(forms.Form):
    text = forms.CharField(max_length=140)
