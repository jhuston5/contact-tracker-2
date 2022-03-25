from django.db import models

# Create your models here.
from unicodedata import name
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Contact(models.Model):
  owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  type = models.CharField(max_length=128)
  location = models.CharField(max_length=32)
  description = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.type