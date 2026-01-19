from django.db import models

# Creamos el modelo
class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    subject = models.CharField(max_length=50)
    messages = models.TextField()

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contact's"