from rest_framework.viewsets import ModelViewSet
from notification.models.email import Email
from notification.models.email_status import EmailStatus
from django.shortcuts import get_object_or_404
from landix.utils import views_utils
from landix.serializers.Generic import GenericReadSerializer
from rest_framework.decorators import action
from rest_framework.schemas import ManualSchema
from rest_framework.request import Request
from rest_framework.response import Response
import coreapi, coreschema


class EmailView(ModelViewSet):
    queryset = Email.objects.all()
    http_method_names = ['get', 'post']
    filter_fields = {
        'mail_from': ['exact'],
        'mail_to': ['in']
    }

    def get_serializer_class(self):
        if self.request.method == "GET":
            serializer_class = views_utils.get_generic_read_serializer(Email, 1)
        else:
            serializer_class = views_utils.get_generic_read_serializer(Email, 0)

        return serializer_class

    @action(methods=["post"],
            detail=False,
            url_path="textmail",
            schema=ManualSchema(fields=[
                coreapi.Field(
                    "mail_from",
                    required=True,
                    location="form",
                    schema=coreschema.String()
                ),
                coreapi.Field(
                    "mail_to",
                    required=True,
                    location="form",
                    schema=coreschema.String()
                ),
                coreapi.Field(
                    "subject",
                    required=True,
                    location="form",
                    schema=coreschema.String()
                ),
                coreapi.Field(
                    "header",
                    required=True,
                    location="form",
                    schema=coreschema.String()
                ),
                coreapi.Field(
                    "body",
                    required=True,
                    location="form",
                    schema=coreschema.String(),
                    description='Body of the email in HTML format'
                )]))
    def send_email_using_default_layout(self, request: Request):
        """Send an email using the default layout"""
        mail_from = views_utils.get_param_or_400(request.data, 'mail_from', str)
        mail_to = views_utils.get_param_or_400(request.data, 'mail_to', str)
        subject = views_utils.get_param_or_400(request.data, 'subject', str)
        header = views_utils.get_param_or_400(request.data, 'header', str)
        body = views_utils.get_param_or_400(request.data, 'body', str)
        status = get_object_or_404(EmailStatus, id=1)

        Email.create_email_using_default_layout(mail_from, mail_to, subject, header, body, status)
        return Response()
