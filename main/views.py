from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CharacterSerializer
from .models import Character


def home(request):
	characters = Character.objects.all()
	return render(request, 'index.html', {'characters': characters})

class CharacterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer