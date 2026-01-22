from django.shortcuts import render, redirect

# Importamos el modelo
from apps.project.models import Project
from apps.contact.models import Contact

# Cargar correo
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
import threading

def send_contact_email(subject, body):
    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        ["nicolas.paulo.vega06@gmail.com"],
        fail_silently=False,
    )

def index(request):
    projects = Project.objects.all()

    if request.method == "POST" and request.headers.get("x-requested-with") == "XMLHttpRequest":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        user_message = request.POST.get("message")

        Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            messages=user_message,
        )

        message = f"""
            Nombre: {name}
            Correo electronico: {email}
            Telefono: {phone}

            {user_message}
        """

        # Enviamos el correo en segundo plano
        threading.Thread(
            target=send_contact_email,
            args=(subject, message),
        ).start()

        # Enviamos respuesta Json:
        return JsonResponse({ "status": "success", "message": "Tu mensaje fue enviado con exito!" })

    return render(request, "index.html", {"projects": projects})