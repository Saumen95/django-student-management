# filters.py

import django_filters
from .models import Note

class NoteFilter(django_filters.FilterSet):
    category = django_filters.NumberFilter(field_name='category__id')

    class Meta:
        model = Note
        fields = ['category']
