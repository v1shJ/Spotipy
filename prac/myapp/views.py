from django.shortcuts import render, HttpResponse
from .models import TodoItem
# Create your views here.
def home(request):
    return render(request, "home.html") #rendering the home.html file
    #return HttpResponse("Hello World") #returning a response

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})
