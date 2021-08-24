from django.shortcuts import render,HttpResponseRedirect
from .models import DataCollected

def post_list(request):
    objects = DataCollected.objects.all()
    #Exampel with filters
    argentinians = DataCollected.objects.filter(location = "Argentina")
    groenlandia = DataCollected.objects.filter(location = "Groenlandia")
    return render(request, 'assesment/post_list.html',{"collected_data": objects, "data_filter": argentinians, "data_locate": groenlandia})

def create_colleted_data(request):
    if request.POST:
        name = request.POST.get("name")
        location = request.POST.get("location")
        tipo = request.POST.get("type")
        email= request.POST.get("email")
        content= request.POST.get("content")
        new_object = DataCollected(name=name, location=location, type=tipo, email=email, content=content)
        new_object.save()
        return HttpResponseRedirect('/')

    return render(request, 'assesment/creation-form.html',{})
