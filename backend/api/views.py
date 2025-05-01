from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer, CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Note, Category
from .filters import NoteFilter
from useranalytics.models import ActivityLog
from dal import autocomplete



class NoteAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Note.objects.all()
        if self.q:
            qs = qs.filter(title__icontains=self.q)
        return qs


class CreateNoteView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NoteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = NoteFilter

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            note = serializer.save(author=self.request.user)
            # Log the creation of the note
            ActivityLog.objects.create(
                user=self.request.user,
                action_type='CREATE',
                status='SUCCESS',
                remarks=f"Note '{note.title}' created"
            )
        else:
            print(serializer.errors)


class CreateCategoryView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer

    def get_queryset(self):
        user = self.request.user
        return Category.objects.filter(user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(user=self.request.user)
        else:
            print(serializer.errors)



class DeleteNoteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NoteSerializer

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)

class CreateuserView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer
