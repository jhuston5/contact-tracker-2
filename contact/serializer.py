from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ('id', 'owner', 'type', 'location', 'description', 'created_at', 'updated_at')
    model = Contact