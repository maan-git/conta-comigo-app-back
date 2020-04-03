from rest_framework.decorators import action
import coreschema
import coreapi
from rest_framework.schemas import ManualSchema, AutoSchema
from rest_framework.viewsets import ModelViewSet
from help.models.help_request import HelpRequest
from rest_framework.request import Request
from rest_framework.response import Response
from help.serializers.help_request_serializer import HelpRequestSerializer
from help.serializers.help_request_serializer import HelpRequestSerializerWrite
from help.serializers.help_request_serializer import HelpStatusRequestSerializer
from rest_framework.exceptions import ParseError
from django.utils.translation import ugettext_lazy as _
from rest_framework import status
from help.models.helping_status import HelpingStatus
from help.models.help_request_status import HelpRequestStatus
from help.models.helprequest_helpers import HelpRequestHelpers

from utils.views_utils import get_param_or_400
from rest_framework.renderers import JSONRenderer


class HelpRequestView(ModelViewSet):
    queryset = HelpRequest.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return HelpRequestSerializer
        else:
            return HelpRequestSerializerWrite

    def get_status_serializer_class(self):
        if self.request.method == "POST":
            return HelpStatusRequestSerializer

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
        if helping_user_relation and \
                helping_user_relation.status_id == HelpingStatus.AllStatus.Helping:
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
            url_path="unapplyownequest",
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
    def unapply_of_own_request(self, request: Request, pk):
        """
        Logged user applies to help in a help request.
        """
        help_request = self.get_object()
        helping_user = self._validate_user_help_relation(request, pk)
        print(pk)

        if helping_user and helping_user.status_id != HelpRequestStatus.AllStatus.Canceled \
                and helping_user.status_id != HelpRequestStatus.AllStatus.Finished:
            helping_user.status_id = HelpRequestStatus.AllStatus.Canceled
            helping_user.save()

        return Response(status=200)



    def _validate_user_relation(self, request: Request, pk):
        helping_user_relation = HelpRequestHelpers.objects.filter(helper_user=request.user).first()

        if not helping_user_relation:
            raise ParseError(detail=_('You are not helping in this request'),
                             code=status.HTTP_400_BAD_REQUEST)
        return helping_user_relation

    def _validate_user_help_relation(self, request: Request, pk):
        helping_user_help_relation = HelpRequest.objects.filter(owner_user=request.user).first()
        if not helping_user_help_relation:
            raise ParseError(detail=_('You are not owner of this post'),
                             code=status.HTTP_400_BAD_REQUEST)
        return helping_user_help_relation
