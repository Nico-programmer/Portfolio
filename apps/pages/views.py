from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from django.core.mail import send_mail

from apps.project.models import Project
from apps.contact.models import Contact


def index(request):
    projects = Project.objects.all()

    # Solo aceptamos POST por AJAX
    if request.method == "POST" and request.headers.get("x-requested-with") == "XMLHttpRequest":
        try:
            name = request.POST.get("name")
            email = request.POST.get("email")
            phone = request.POST.get("phone")
            subject = request.POST.get("subject")
            user_message = request.POST.get("message")

            # Guardamos el contacto
            Contact.objects.create(
                name=name,
                email=email,
                phone=phone,
                subject=subject,
                messages=user_message,
            )

            message = (
                f"Nombre: {name}\n"
                f"Correo: {email}\n"
                f"Teléfono: {phone}\n\n"
                f"Mensaje:\n{user_message}"
            )

            # Envío del correo (SIN threading)
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=["nicolas.paulo.vega06@gmail.com"],
                reply_to=[email],
                fail_silently=False,
            )

            return JsonResponse({
                "status": "success",
                "message": "Tu mensaje fue enviado con éxito ✅"
            })

        except Exception as e:
            # Log real (útil en Railway)
            print("ERROR EMAIL:", e)

            return JsonResponse({
                "status": "error",
                "message": "No se pudo enviar el mensaje ❌"
            }, status=500)

    return render(request, "index.html", {"projects": projects})