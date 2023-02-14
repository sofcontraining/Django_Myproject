from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("This is Home page")
    return render(request, 'home.html')

def about(request):
  #  return HttpResponse("This is About page")
     return render(request, 'about.html')
def services(request):
    #return HttpResponse("This is Serives page")
    return render(request, 'services.html')
def contact(request):
    #return HttpResponse("This is Contact page")
    return render(request, 'contact.html')