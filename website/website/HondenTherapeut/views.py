from django.http import HttpResponse


# Create your views here.
def courses(request):
    return HttpResponse(
        '<h1>Homepage</h1>'
    )
