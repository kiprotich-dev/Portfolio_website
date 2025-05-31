from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=30)

    def __str__(self):
        return self.name