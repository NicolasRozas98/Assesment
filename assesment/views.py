from django.shortcuts import render,HttpResponseRedirect
from .models import DataCollected
from django.core.mail import send_mail
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def post_list(request):
    #Collect All the objects
    objects = DataCollected.objects.all()
    #Example with filters
    argentinians = DataCollected.objects.filter(location = "Argentina")
    groenlandia = DataCollected.objects.filter(location = "Groenlandia")
    return render(request, 'assesment/creation-form.html',{"collected_data": objects,
                                                        "data_filter": argentinians,
                                                        "data_locate": groenlandia, })

    #Create Form and send Email
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
                                                                     'email':email})
        plain_message = strip_tags(html_message)
        # send the Email 
        send_mail(
            tipo,
            plain_message,
            'nicolasrozas22@gmail.com',
            [email],
            fail_silently = False,
            html_message = html_message,
        )
        return HttpResponseRedirect('/')

    return render(request, 'assesment/creation-form.html',{})
