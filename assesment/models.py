from django.db import models


class DataCollected(models.Model):
    BOOK_CHOICES = (
        ("general_enquiry", "General Enerquy"),
        ("request_a_call_back", "Request A Call Back"),
        ("customer_service_enquiry", "Customer Service Enquiry"),
    )
    type = models.CharField(max_length= 100, choices= BOOK_CHOICES)
    name = models.CharField(max_length=64, default="")
    content = models.TextField(max_length=500, null=True)
    location = models.CharField(max_length=64, default="")
    email = models.EmailField(max_length=254, default="")
    
