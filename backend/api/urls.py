from django.urls import path
from . import views
from .views import NoteAutocomplete

urlpatterns = [
    path('notes/', views.CreateNoteView.as_view(), name='create_note'),
    path('notes/<int:pk>/', views.DeleteNoteView.as_view(), name='delete_note'),
    path('category/', views.CreateCategoryView.as_view(), name='create_category'),
    path('note-autocomplete/', NoteAutocomplete.as_view(), name='note-autocomplete')
]
