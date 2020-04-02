from rest_framework.decorators import action
import coreschema
import coreapi
from rest_framework.schemas import ManualSchema, AutoSchema
from rest_framework.viewsets import ModelViewSet
from help.models.help_request import HelpRequest
from requests import Request
from rest_framework.response import Response
from help.serializers.help_request_serializer import HelpRequestSerializer
from help.serializers.help_request_serializer import HelpRequestSerializerWrite
from rest_framework.exceptions import ParseError
from django.utils.translation import ugettext_lazy as _
from rest_framework import status
from help.models.helping_status import HelpingStatus
from help.models.help_request_status import HelpRequestStatus
from help.models.helprequest_helpers import HelpRequestHelpers

from utils.views_utils import get_param_or_400


class HelpRequestView(ModelViewSet):
    queryset = HelpRequest.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return HelpRequestSerializer
        else:
            return HelpRequestSerializerWrite

    @action(methods=["post"],
            detail=True,
            url_path="candidatetohelp",
            schema=ManualSchema(fields=[
                coreapi.Field(
                    "id",
                    required=True,
                    location="path",
                    schema=coreschema.Integer()
                )])
            )
    def candidate_to_help(self, request: Request, pk):
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
            url_path="giveuphelp",
            schema=ManualSchema(fields=[
                coreapi.Field(
                    "id",
                    required=True,
                    location="path",
                    schema=coreschema.Integer()
                )])
            )
    def give_up_help(self, request: Request, pk):
        helping_user_relation = HelpRequestHelpers.objects.filter(helper_user=request.user).first()

        if not helping_user_relation:
            raise ParseError(detail=_('You are not helping in this request'),
                             code=status.HTTP_400_BAD_REQUEST)

        helping_user_relation.status_id = HelpingStatus.AllStatus.Canceled
        helping_user_relation.save()

        return Response(status=200)

    """
    • Criado → Cancelado
    --• Criado → Em andamento--
    • Em andamento → Cancelado    
    • Em andamento → Finalizado
    
    Created = 1
    InProgress = 20
    Canceled = 99
    Finished = 100
    """

    # Working on
    @action(methods=["POST"],
            detail=True,
            url_path="updatestatushelp",
            schema=ManualSchema(fields=[
                coreapi.Field(
                    "id",
                    required=True,
                    location="body",
                    schema=coreschema.Integer()
                ),
                coreapi.Field(
                    "status_id",
                    required=True,
                    location="body",
                    schema=coreschema.Integer()
                )
            ])
            )
    def update_status_help(self, request: Request, pk):
        help_request = self.get_object()
        status_id = get_param_or_400(request.data, 'status_id', int)
        print(help_request)
        print(status_id)

        # helping_user_help_relation = self._validate_user_help_relation(request, pk)
        #
        # if helping_user_help_relation.status_id == HelpRequestStatus.AllStatus.Created and \
        #         status_id == HelpRequestStatus.AllStatus.Canceled:
        #     helping_user_help_relation.status_id = HelpRequestStatus.AllStatus.Canceled
        #     helping_user_help_relation.save()
        #
        # elif helping_user_help_relation.status_id == HelpRequestStatus.AllStatus.InProgress and \
        #         (status_id == HelpRequestStatus.AllStatus.Canceled or \
        #          status_id == HelpRequestStatus.AllStatus.Finished):
        #     helping_user_help_relation.status_id = list(filter(lambda x: request['status_id'] == x,
        #                                                        HelpRequestStatus.AllStatus))[0]
        #     helping_user_help_relation.save()
        # else:
        #     raise ParseError(detail=_('You cannot make this operation'),
        #                      code=status.HTTP_400_BAD_REQUEST)

        return Response(status=200)

    def _validate_user_relation(self, request: Request, pk):
        helping_user_relation = HelpRequestHelpers.objects.filter(helper_user=request.user).first()

        if not helping_user_relation:
            raise ParseError(detail=_('You are not helping in this request'),
                             code=status.HTTP_400_BAD_REQUEST)
        return helping_user_relation

    # def _validate_user_help_relation(self, request: Request, pk):
    #     helping_user_help_relation = HelpRequest.objects.filter(owner_user=request.user).first()
    #     if not helping_user_help_relation:
    #         raise ParseError(detail=_('You are not owner of this post'),
    #                          code=status.HTTP_400_BAD_REQUEST)
    #     return helping_user_help_relation
