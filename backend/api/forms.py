from dal import autocomplete
from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title',)
        widgets = {
            'title': autocomplete.ModelSelect2(url='note-autocomplete')
        }
