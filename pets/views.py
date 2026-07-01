from django.http import HttpResponse

# Create your views here.
def pet_list(request):
    return HttpResponse("List of pets")