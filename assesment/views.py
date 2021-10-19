from django.shortcuts import render
from .forms import DataForm
from django.views.generic.edit import FormView
from django.contrib import messages


class DataFormView(FormView):
    template_name = 'assesment/creation-form.html'
    form_class = DataForm

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'Email sent successfully')
        return super().form_valid(form)

    def get_success_url(self): 
        return self.request.path


def index(request):
    form = DataForm
    context = {'form':form}
    return render(request, 'assesment/creation-form.html',context)
