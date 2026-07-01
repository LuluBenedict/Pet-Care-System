from django.http import HttpResponse

# Create your views here.
def service_home(request):
    return HttpResponse("Welcome to the Petcare Home Page!")
