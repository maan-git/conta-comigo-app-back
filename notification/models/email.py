from django.db import models as django_models
from notification.models.email_status import EmailStatus
from utils.templates_helper import render_template


class Email(django_models.Model):
    mail_from = django_models.CharField("Remetente", max_length=300, null=False)
    mail_to = django_models.TextField("Destinatario", null=False)
    subject = django_models.CharField("Assunto", max_length=300)
    content = django_models.TextField("Mensagem")
    status = django_models.ForeignKey(
        "EmailStatus",
        on_delete=django_models.DO_NOTHING,
        related_name='Status',
        related_query_name="Status",
        null=False
    )
    error_message = django_models.TextField("Mensagem de erro", null=True)

    def __str__(self):
        return self.mail_from

    @classmethod
    def create_email_using_default_layout(cls, mail_from, mail_to, subject, header, body, status):
        for destiny in mail_to.split(','):
            email_html = EmailLib.render_template('emails/alteracao_avaliacao.html',
                                                  {'user': destiny.split('@')[0], 'header': header, 'mensagem': body})

            if email_html is None:
                print('Falha ao renderizar template')
                return

            new_email = Email()

            new_email.mail_from = mail_from
            new_email.mail_to = destiny
            new_email.subject = subject
            new_email.content = str(email_html)
            new_email.status = status
            new_email.save()

    @classmethod
    def create_email_evaluation_edited(cls, mail_to):
        body = 'Você está recebendo esta mensagem porque uma de suas avaliação foi alterada recentemente no Ldxtools.'
        mail_from = 'leandrocarneiro@landix.com.br'
        subject = 'Avaliação alterada'
        status = EmailStatus.objects.get(id=1)

        Email.create_email_using_default_layout(mail_from, mail_to, subject, '', body, status)
