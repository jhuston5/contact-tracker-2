from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from .serializer import ContactSerializer
from .permissions import IsOwnerOrReadOnly
from .models import Contact
from rest_framework.permissions import IsAuthenticated
# Create your views here

# class ContactList(generics.ListAPIView)

# queryset = Contact.objects.all()

# serializer_class = ContactSerializer

class ContactList(generics.ListCreateAPIView):
  permission_classes = (IsAuthenticated,)
  queryset = Contact.objects.all()
  serializer_class = ContactSerializer

class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsAuthenticated,)
  queryset = Contact.objects.all()
  serializer_class = ContactSerializer

