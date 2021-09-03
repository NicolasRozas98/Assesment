from django.shortcuts import render
from .models import DataCollected
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib import messages

#Creates Form and sends Email
def create_colleted_data(request):
    if request.POST:
        name = request.POST.get("name")
        location = request.POST.get("location")
        tipo = request.POST.get("type_choice")
        email= request.POST.get("email")
        content= request.POST.get("content")
        html_message = render_to_string('assesment/base_email.html',{'location': location,
                                                                     'name':name,
                                                                     'content':content,
                                                                     'type_choice':tipo,
                                                                     'email':email,})
        plain_message = strip_tags(html_message)
        # Send the Email  success :D
        messages.success(request, 'Email sent successfully')
        send_mail(
            tipo,
            plain_message,
            'nicolasrozas22@gmail.com',
            [email],
            fail_silently = False,
            html_message = html_message,
        )

    return render(request, 'assesment/creation-form.html',{})
