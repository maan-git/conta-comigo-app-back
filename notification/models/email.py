import logging
from django.db import models as django_models
from notification.models.email_status import EmailStatus
from utils.templates_helper import render_template
from django.utils.translation import ugettext_lazy as _


class Email(django_models.Model):
    sender = django_models.CharField(_("Sender"), max_length=300, null=False)
    recipient = django_models.TextField(_("Recipient"), null=False)
    subject = django_models.CharField(_("Subject"), max_length=300)
    content = django_models.TextField(_("HTML content"))
    status = django_models.ForeignKey(
        EmailStatus,
        on_delete=django_models.DO_NOTHING,
        related_name='status',
        null=False
    )
    error_message = django_models.TextField(_("Error message"), null=True, blank=True)

    def __str__(self) -> str:
        return self.subject


def create_email(sender: str, recipient: str, subject: str, template: str, render_data: dict) -> Email:
    email_html = render_template(template, render_data)

    if email_html is None:
        logging.error(_('System has failed to create email from template "%s" with data "%s"'),
                      template,
                      render_data)
        return None

    new_email = Email()

    new_email.sender = sender
    new_email.recipient = recipient
    new_email.subject = subject
    new_email.content = email_html
    new_email.status_id = EmailStatus.AllStatus.WAITING
    new_email.save()
    return new_email
