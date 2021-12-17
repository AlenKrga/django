from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world, this is index of polls.")

# Create your views here.
