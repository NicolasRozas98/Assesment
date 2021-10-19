from django.forms import ModelForm
from .models import DataCollected
from .models import DataCollected
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


class DataForm(ModelForm): #This class inherits from the Data Collected model all data 
    class Meta:
        model = DataCollected
        fields = '__all__'
    
    def send_email(self):
        """
        Sends Email and created and object in the database 
        """
        name = self.cleaned_data.get("name")
        location = self.cleaned_data.get("location")
        tipo = self.cleaned_data.get("type_choice")
        email= self.cleaned_data.get("email")
        content = self.cleaned_data.get("content")

        html_message = render_to_string(
            'assesment/base_email.html',
            {
                'location': location,
                'name':name,
                'content':content,
                'type_choice':tipo,
                'email':email,
            }
        )
        plain_message = strip_tags(html_message)

        send_mail(
            tipo, #This is the subject
            plain_message, #This is the message
            'nicolasrozas22@gmail.com', # This is the recipient who sends the email
            [email],
            fail_silently = False,
            html_message = html_message,
        )
        #This "data_collected" is for save the data in the database
        data_collected = DataCollected(
            name = name,
            location = location,
            type_choice = tipo,
            email = email,
            content = content,
        )
        data_collected.save()


