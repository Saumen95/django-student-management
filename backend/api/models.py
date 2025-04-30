from django.db import models
from django.contrib.auth.models import User
import uuid
from django.urls import reverse
from django.utils.functional import cached_property

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)
    is_shared = models.BooleanField(default=False)
    share_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    @property
    def is_shared_note(self):
            """
            Returns True if the note is marked as shared.
            """
            return self.is_shared


    @cached_property
    def get_share_link(self, request):
            """
            Returns the full URL to access the shared note.
            """
            if self.is_shared:
                relative_url = reverse('shared-note', kwargs={'share_uuid': self.share_uuid})
                return request.build_absolute_uri(relative_url)
            return None

    def __str__(self):
        return self.title

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="categories")
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name




