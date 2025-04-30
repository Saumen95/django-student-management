from django.shortcuts import render
from .models import SharedNote
from .serializers import SharedNoteSerializer
from rest_framework import generics


class SharedNoteCreateView(generics.CreateAPIView):
    queryset = SharedNote.objects.all()
    serializer_class = SharedNoteSerializer

class SharedNoteDetailView(generics.RetrieveAPIView):
    queryset = SharedNote.objects.filter(is_active=True)
    serializer_class = SharedNoteSerializer
    lookup_field = 'share_uuid'
