from django.core.mail import EmailMessage
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render

from apps.project.models import Project
from apps.contact.models import Contact


def index(request):
    projects = Project.objects.all()

    if request.method == "POST" and request.headers.get("x-requested-with") == "XMLHttpRequest":
        try:
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

            body = (
                f"Nombre: {name}\n"
                f"Correo: {email}\n"
                f"Teléfono: {phone}\n\n"
                f"Mensaje:\n{user_message}"
            )

            email_message = EmailMessage(
                subject=subject,
                body=body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=["nicolas.paulo.vega06@gmail.com"],
                reply_to=[email],
            )

            email_message.send(fail_silently=False)

            return JsonResponse({
                "status": "success",
                "message": "Tu mensaje fue enviado con éxito ✅"
            })

        except Exception as e:
            print("ERROR EMAIL:", e)
            return JsonResponse({
                "status": "error",
                "message": "No se pudo enviar el mensaje ❌"
            }, status=500)

    return render(request, "index.html", {"projects": projects})