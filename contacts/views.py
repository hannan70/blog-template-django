from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from django.contrib import messages


# Create your views here.
def contact_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # name = form.cleaned_data['name']
            # email = form.cleaned_data['email']
            # message = form.cleaned_data['message']
            # new_contact = Contact(name=name, email=email, message=message)
            # new_contact.save()
            form.save()
            messages.success(request, "Message Send Success")
            return redirect('/contact/')
        else:
            messages.error(request, "Something is wring")
    else:
        form = ContactForm()
    return render(request, 'pages/contact.html', {"form": form})
