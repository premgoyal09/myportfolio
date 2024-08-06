from django.shortcuts import render, HttpResponse

# Create your views here.
from portfolio_App.models import Contact
from django.contrib import messages

# from .forms import SignupForm

def home(request):
    return render(request, 'data/home.html')

def about(request):
    return render(request, 'data/about.html')

def skills(request):
    return render(request, 'data/skills.html')

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        print(name, email, phone, content)
        
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "please fill the form attentively ")
        else:
            contact = Contact(name=name, email=email, phone=phone)
            contact.save()      
            messages.success(request, "thanks you , your messages was sent sucessfully")
    return render(request, 'data/contact.html')
  

