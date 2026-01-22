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
                from_email="Contacto Web <nicolas.paulo.vega06@gmail.com>",
                to_emails="nicolas.paulo.vega06@gmail.com",
                subject=f"Nuevo mensaje desde tu portafolio: {subject}",
                plain_text_content=f"""
                    Hola Nicolás,

                    Has recibido un nuevo mensaje a través del formulario de contacto de tu portafolio web.

                    A continuación encontrarás los datos proporcionados por la persona que se comunicó contigo:

                    Nombre completo:
                    {name}

                    Correo electrónico de contacto:
                    {email}

                    Número de teléfono:
                    {phone}

                    Mensaje enviado:
                    {user_message}

                    Este mensaje fue generado automáticamente desde tu sitio web.
                    Puedes responder directamente a este correo para contactar a la persona interesada.

                    Saludos,
                    Sistema de contacto de tu portafolio
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