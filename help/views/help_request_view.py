from rest_framework.decorators import action
import coreschema
import coreapi
from rest_framework.schemas import ManualSchema
from rest_framework.viewsets import ModelViewSet
from help.models.help_request import HelpRequest
from rest_framework.request import Request
from rest_framework.response import Response
from help.serializers.help_request_serializer import HelpRequestSerializer
from help.serializers.help_request_serializer import HelpRequestSerializerWrite
from rest_framework.exceptions import ParseError
from django.utils.translation import ugettext_lazy as _
from rest_framework import status
from help.models.helping_status import HelpingStatus
from help.models.helprequest_helpers import HelpRequestHelpers


class HelpRequestView(ModelViewSet):
    queryset = HelpRequest.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return HelpRequestSerializer
        else:
            return HelpRequestSerializerWrite

    @action(methods=["post"],
            detail=True,
            url_path="applytohelp",
            schema=ManualSchema(description='Logged user applies to help in a help request',
                                fields=[
                                    coreapi.Field(
                                        "id",
                                        required=True,
                                        location="path",
                                        schema=coreschema.Integer(),
                                        description='Help request ID'
                                    )])
            )
    def apply_to_help(self, request: Request, pk):
        """
        Logged user applies to help in a help request.
        """
        help_request = self.get_object()

        if help_request.owner_user == request.user:
            raise ParseError(detail=_('You can not help in your own request'),
                             code=status.HTTP_400_BAD_REQUEST)

        helping_user_relation = HelpRequestHelpers.objects.filter(helper_user=request.user).first()

        # TODO In the future this may be removed since we will allow more users
        if helping_user_relation and helping_user_relation.status_id == HelpingStatus.AllStatus.Helping:
            raise ParseError(detail=_('Another user is already helping in the request'),
                             code=status.HTTP_400_BAD_REQUEST)

        if helping_user_relation and helping_user_relation.status_id == HelpingStatus.AllStatus.Helping:
            raise ParseError(detail=_('You are already helping in this request'),
                             code=status.HTTP_400_BAD_REQUEST)

        if not helping_user_relation:
            help_request.helping_users.add(request.user)
        else:
            helping_user_relation.status_id = HelpingStatus.AllStatus.Helping
            helping_user_relation.save()

        return Response(status=200)

    @action(methods=["post"],
            detail=True,
            url_path='unapplyfromhelp',
            schema=ManualSchema(description='Logged user unapply from a help request',
                                fields=[
                                    coreapi.Field(
                                        'id',
                                        required=True,
                                        location='path',
                                        schema=coreschema.Integer(),
                                        description='Help request ID'
                                    )])
            )
    def unapply_from_help(self, request: Request, pk):
        helping_user_relation = HelpRequestHelpers.objects.filter(helper_user=request.user).first()

        if not helping_user_relation:
            raise ParseError(detail=_('You are not helping in this request'),
                             code=status.HTTP_400_BAD_REQUEST)

        helping_user_relation.status_id = HelpingStatus.AllStatus.Canceled
        helping_user_relation.save()

        return Response(status=200)

    @action(methods=["post"],
            detail=True,
            url_path="changestatusrequest",
            schema=ManualSchema(fields=[
                coreapi.Field(
                    "id",
                    required=True,
                    location="path",
                    schema=coreschema.Integer()
                ),
                coreapi.Field(
                    "status_id",
                    required=True,
                    location="path",
                    schema=coreschema.Integer()
                )])
            )
    def change_status_request(self, request: Request, pk):
        helping_user_relation = HelpRequestHelpers.objects.filter(helper_user=request.user).first()

        if not helping_user_relation:
            raise ParseError(detail=_('You are not helping in this request'),
                             code=status.HTTP_400_BAD_REQUEST)

        try:
            helping_user_relation.status_id = request['status_id']
        except:
            raise ParseError(detail=_('Status id is invalid'),
                             code=status.HTTP_400_BAD_REQUEST)

        return Response(status=200)
