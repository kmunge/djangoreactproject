from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField("First name", max_length = 100)
    last_name = models.CharField("Last name", max_length = 100)
    email = models.EmailField()
    phone = models.CharField(max_length = 10)
    address = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    createdAt = models.DateTimeField("Created At", auto_now_add=True)


    def __str__(self):
        return self.first_name