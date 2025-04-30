from django.urls import path
from .views import SharedNoteCreateView, SharedNoteDetailView


urlpatterns = [
    path('share/', SharedNoteCreateView.as_view(), name='share-note'),
    path('share/<uuid:share_uuid>/', SharedNoteDetailView.as_view(), name='shared-note-detail'),
]
