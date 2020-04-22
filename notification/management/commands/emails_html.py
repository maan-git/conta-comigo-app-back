from django.core.mail import send_mail
from notification.management.commands.emails import Emails


class EmailsHtml(Emails):

    def mount_email(self, email):
        send_mail(
            email.subject,
            "",
            email.mail_from,
            [email.mail_to],
            fail_silently=False,
            html_message=email.content
        )
