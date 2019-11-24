from django import forms

class formUrl(forms.Form):
    youtubeUrl = forms.CharField(label='Youtube URL', max_length=500, required=True)
