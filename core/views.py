from django.shortcuts import render, redirect
from core.models import ContactUs
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings


# Create your views here.

def email(request):
    return render(request, "core/email.html")

def index(request):

    if request.method == 'POST':
        
        form = ContactUs(
            name=request.POST['name'],
            email=request.POST['email'],
            message=request.POST['message'],
          
        )
        form.save()

        html_template = 'core/email.html'
        html_message = render_to_string('core/email.html', {'form': form})
            #html_message = render_to_string(html_template)
        subject = 'Marizu'
        email_form = settings.EMAIL_HOST_USER
        recipient_list = ['tobemarizu@gmail.com']
        message = EmailMessage(subject, html_message,
                                   email_form, recipient_list)
        message.content_subtype = 'html'
        message.send()
        
        messages.success(request, "Message sent Successfully. We will get back to You")
        return redirect("core:index")
    else:
        
         return render(request, "core/index.html")

   
