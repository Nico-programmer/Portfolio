from django.shortcuts import render
from django.http import JsonResponse
from apps.project.models import Project
from apps.contact.models import Contact
import os

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


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

            message = Mail(
                from_email="nicolas.paulo.vega06@gmail.com",
                to_emails="nicolas.paulo.vega06@gmail.com",
                subject=subject,
                plain_text_content=f"""
                    Nombre: {name}
                    Correo: {email}
                    Teléfono: {phone}

                    Mensaje:
                    {user_message}
                """,
            )

            message.reply_to = email

            sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))
            sg.send(message)

            return JsonResponse({
                "status": "success",
                "message": "Mensaje enviado correctamente ✅"
            })

        except Exception as e:
            print("SENDGRID ERROR:", e)
            return JsonResponse({
                "status": "error",
                "message": "Error al enviar el mensaje ❌"
            }, status=500)

    return render(request, "index.html", {"projects": projects})