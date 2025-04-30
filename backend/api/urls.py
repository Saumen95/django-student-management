from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.CreateNoteView.as_view(), name='create_note'),
    path('notes/<int:pk>/', views.DeleteNoteView.as_view(), name='delete_note')
]
