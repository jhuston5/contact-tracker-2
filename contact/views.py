from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from .serializer import ContactSerializer
from .permissions import IsOwnerOrReadOnly
from .models import Contact

# Create your views here

# class ContactList(generics.ListAPIView)

# queryset = Contact.objects.all()

# serializer_class = ContactSerializer

class ContactList(generics.ListCreateAPIView):
  permission_classes = (IsOwnerOrReadOnly,)
  queryset = Contact.objects.all()
  serializer_class = ContactSerializer

class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsOwnerOrReadOnly,)
  queryset = Contact.objects.all()
  serializer_class = ContactSerializer

