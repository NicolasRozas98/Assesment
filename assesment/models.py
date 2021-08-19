from django.db import models


class DataCollected(models.Model):
    BOOK_CHOICES = (
        ("General Enquiry", "General Enerquy"),
        ("Request A Call Back", "Request A Call Back"),
        ("Customer Service Enquiry", "Customer Service Enquiry"),
    )
    type = models.CharField(max_length= 100, choices= BOOK_CHOICES)

    name = models.TextField(max_length=64, null=True)
    location = models.TextField(max_length=64, null=True)
