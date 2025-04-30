from rest_framework import serializers
from .models import SharedNote


class SharedNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SharedNote
        fields = ['share_uuid', 'note', 'is_active', 'created_at']
