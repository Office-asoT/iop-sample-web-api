from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings

class SendTestMail(APIView):

    def post(self, request, user_id):
        to_email = request.data['email_address']
        subject = settings.MAIL_CONTENT['TEST_MAIL']['SUBJECT']
        message = settings.MAIL_CONTENT['TEST_MAIL']['MESSAGE']

        email = Mail(
            from_email=settings.DEFAULT_FROM_EMAIL,
            to_emails=to_email,
            subject=subject,
            html_content=message,
        )

        try:
            sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
            response = sg.send(email)
            return Response(status=response.status_code)
        
        except Exception as e:
            return Response({"error": str({e})}, status=500)
