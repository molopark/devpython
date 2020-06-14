from http import HttpResponse

def index(request):
    return HttpResponse("Hello")
