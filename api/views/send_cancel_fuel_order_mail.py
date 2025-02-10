from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings

class SendCancelFuelOrderMail(APIView):

    def post(self, request, user_id):
        to_email = request.data['email_address']
        email_data = {
            "ja_branch_office_name": request.data['ja_branch_office_name'],
            "order_date": request.data['order_date'],
            "user_id": user_id,
            "farm_field_name": request.data['farm_field_name'],
            "fuel_type": request.data['fuel_type'],
            "quantity": request.data['quantity']
        }

        subject = settings.MAIL_CONTENT['CANCEL_FUEL_ORDER_MAIL']['SUBJECT']
        message_template = settings.MAIL_CONTENT['CANCEL_FUEL_ORDER_MAIL']['MESSAGE']

        message = message_template.format(**email_data)
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
