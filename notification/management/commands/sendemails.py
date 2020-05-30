import logging
from django.core.management.base import BaseCommand
from notification.models.email import Email
from django.core.mail import send_mail
from notification.models.email_status import EmailStatus


class Command(BaseCommand):
    help = 'Send all emails'

    @classmethod
    def _send_email(cls, email: Email):
        try:
            send_mail(
                email.subject,
                "",
                email.sender,
                [email.recipient],
                fail_silently=False,
                html_message=email.content
            )

            email.status_id = EmailStatus.AllStatus.SUCCESSFULLY_SEND
            email.error_message = None
            email.save()
        except Exception as e:
            logging.exception('Exception while sending email "%s"', email.id)
            email.status_id = EmailStatus.AllStatus.ERROR_SEND
            email.error_message = str(e)
            email.save()

    def handle(self, *args, **options):
        emails_to_send = Email.objects.exclude(status=EmailStatus.AllStatus.SUCCESSFULLY_SEND)

        for email in emails_to_send:
            self._send_email(email)
