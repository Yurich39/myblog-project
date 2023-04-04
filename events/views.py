from django.shortcuts import render
from .models import Event

# Create your views here.
def home(request):
	events = Event.objects #получаем из базы данных все обьекты events
	return render(request, 'events/home.html', {'events':events})