from django import forms
from .models import Event
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["title","content","event_image"]