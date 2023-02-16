from django.shortcuts import render, HttpResponse
from . models import Member

# Create your views here.
def home(request):
    all_members = Member.objects.all
    # return HttpResponse("This is Home page")
    return render(request, 'home.html',{'all':all_members})
def about(request):
  #  return HttpResponse("This is About page")
     return render(request, 'about.html')
def services(request):
    #return HttpResponse("This is Serives page")
    return render(request, 'services.html')
def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        city = request.POST['city']
        details = Member(name=name, email=email, contact=contact, city=city)  
        details.save()      
    #return HttpResponse("This is Contact page")
    return render(request, 'contact.html')