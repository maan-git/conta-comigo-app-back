from django.core.management.base import BaseCommand
from notification.models.email import Email
from notification.management.commands.emails_html import EmailsHtml
from notification.models.email_status import EmailStatus


class Command(BaseCommand):
    help = 'Send all emails'

    def handle(self, *args, **options):
        emails_to_send = Email.objects.exclude(status=EmailStatus.AllStatus.SUCCESSFULLY_SEND)

        for email in emails_to_send:
            try:
                EmailsHtml().mount_email(email)

                email.status_id = EmailStatus.AllStatus.SUCCESSFULLY_SEND
                email.error_message = ''
                email.save()
            except Exception as e:
                email.status_id = EmailStatus.AllStatus.ERROR_SEND
                email.error_message = str(e)
                email.save()
