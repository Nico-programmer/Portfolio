from django.shortcuts import render, redirect

# Importamos el modelo
from apps.project.models import Project
from apps.contact.models import Contact

# Cargar correo
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse

def index(request):
    projects = Project.objects.all()

    if request.method == "POST":
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
            messages=user_message
        )

        try:
            send_mail(
                subject,
                f"""
                    Nombre: {name}
                    Email: {email}
                    Telefono: +57 {phone}

                    Mensaje:
                    {user_message}
                """,
                settings.DEFAULT_FROM_EMAIL,
                ["nicolas.paulo.vega06@gmail.com"],
                fail_silently=False,
            )

            # 👇 RESPUESTA AJAX
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({
                    "status": "success",
                    "message": "Tu mensaje fue enviado con éxito ✅"
                })

            messages.success(request, "Tu mensaje fue enviado con éxito!")
        except Exception:
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({
                    "status": "error",
                    "message": "Error al enviar el mensaje ❌"
                }, status=400)
            
            print(e)

            messages.error(request, "Error al enviar el mensaje")

    return render(request, "index.html", {"projects": projects})