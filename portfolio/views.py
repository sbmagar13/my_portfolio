from django.shortcuts import render
from django.http import HttpResponseRedirect
from portfolio.forms import ContactForm
from blogs.models import Post
from works.models import Work
from portfolio.models import Contact
from django.urls import reverse
# Create your views here.

def home(request):
    
    posts = Post.objects.filter(status=1).order_by('-created_on')[:3]
    works = Work.objects.filter(status=1).order_by('-created_on')[:3]
    
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('thanks',))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()
    
    
    return render(request, 'index.html', {'form': form, 'posts': posts, 'works': works})

def thanks(request):
    contacts = Contact.objects.all().order_by('-created')[:1]
    
    return render(request, 'thanks.html', {'contacts': contacts,})