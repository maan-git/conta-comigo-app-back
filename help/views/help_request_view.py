from rest_framework.decorators import action
import coreschema
import coreapi
from rest_framework.schemas import ManualSchema
from help.models.help_request import HelpRequest
from rest_framework.request import Request
from rest_framework.response import Response
from help.serializers.help_request_serializer import HelpRequestSerializer
from help.serializers.help_request_serializer import HelpRequestSerializerWrite
from rest_framework.exceptions import ParseError
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext as _non_lazy
from rest_framework import status
from help.models.helping_status import HelpingStatus
from help.models.help_request_status import HelpRequestStatus
from help.models.helprequest_helpers import HelpRequestHelpers
from django.db import transaction
from utils.views_utils import get_param_or_400
from utils.views_utils import ModelViewSetNoDelete


help_request_field_desc = _non_lazy("Help request ID")


class HelpRequestView(ModelViewSetNoDelete):
    def get_serializer_class(self):
        if self.request.method == "GET":
            return HelpRequestSerializer
        else:
            return HelpRequestSerializerWrite

    def get_queryset(self):
        queryset = HelpRequest.objects.all()

        if not self.request.user.is_superuser and self.request.method != "GET":
            queryset = queryset.filter(owner_user=self.request.user)
        # TODO check other cases (e.g. requests user is helping in)

        return queryset

    @action(
        methods=["post"],
        detail=True,
        url_path="applytohelp",
        schema=ManualSchema(
            description="Logged user applies to help in a help request",
            fields=[
                coreapi.Field(
                    "id",
                    required=True,
                    location="path",
                    schema=coreschema.Integer(),
                    description=help_request_field_desc,
                )
            ],
        ),
    )
    @transaction.atomic
    def apply_to_help(self, request: Request, pk):
        """
        Logged user applies to help in a help request.
        """
        # Lock database row to control concurrency in status update
        help_request = HelpRequest.objects.select_for_update().get(id=pk)

        if help_request.owner_user == request.user:
            raise ParseError(
                detail=_("You can not help in your own request"),
                code=status.HTTP_400_BAD_REQUEST,
            )

        if help_request.finished:
            raise ParseError(
                detail=_("You can not help in finished/canceled requests"),
                code=status.HTTP_400_BAD_REQUEST,
            )

        helping_user_relation = HelpRequestHelpers.objects.filter(
            help_request=help_request, status_id=HelpingStatus.AllStatus.Helping
        ).first()

        if helping_user_relation:
            if helping_user_relation.helper_user == request.user:
                raise ParseError(
                    detail=_("You are already helping in this request"),
                    code=status.HTTP_400_BAD_REQUEST,
                )
            else:
                # TODO In the future this may be removed since we will allow more users
                raise ParseError(
                    detail=_("Another user is already helping in the request"),
                    code=status.HTTP_400_BAD_REQUEST,
                )

        if not helping_user_relation:
            # This didn't work: help_request.helping_users.add(request.user)
            # The post_save signal was not being called in the HelpRequestHelpers class
            HelpRequestHelpers.objects.create(
                help_request=help_request, helper_user=request.user
            )
        else:
            helping_user_relation.status_id = HelpingStatus.AllStatus.Helping
            helping_user_relation.save()

        return Response(status=200)

    @action(
        methods=["post"],
        detail=True,
        url_path="unapplyfromhelp",
        schema=ManualSchema(
            description="Logged user unapply from a help request",
            fields=[
                coreapi.Field(
                    "id",
                    required=True,
                    location="path",
                    schema=coreschema.Integer(),
                    description=help_request_field_desc,
                )
            ],
        ),
    )
    @transaction.atomic
    def unapply_from_help(self, request: Request, pk):
        # Lock database row to control concurrency in status update
        help_request = HelpRequest.objects.select_for_update().get(id=pk)

        helping_user_relation = HelpRequestHelpers.objects.filter(
            help_request=help_request, status_id=HelpingStatus.AllStatus.Helping
        ).first()

        if not helping_user_relation:
            raise ParseError(
                detail=_("You are not helping in this request"),
                code=status.HTTP_400_BAD_REQUEST,
            )

        if help_request.finished:
            raise ParseError(
                detail=_("You can not unapply from finished requests"),
                code=status.HTTP_400_BAD_REQUEST,
            )

        helping_user_relation.status_id = HelpingStatus.AllStatus.Canceled
        helping_user_relation.save()

        return Response(status=200)

    @action(
        methods=["post"],
        detail=True,
        url_path="cancelrequest",
        schema=ManualSchema(
            description="Request owner cancels the request",
            fields=[
                coreapi.Field(
                    "id",
                    required=True,
                    location="path",
                    schema=coreschema.Integer(),
                    description=help_request_field_desc,
                ),
                coreapi.Field(
                    "reasonId",
                    required=True,
                    location="form",
                    schema=coreschema.Integer(),
                    description="Cancellation reason ID",
                ),
            ],
        ),
    )
    @transaction.atomic
    def cancel_request(self, request: Request, pk):
        # Lock database row to control concurrency in status update
        queryset = self.get_queryset()
        try:
            help_request = queryset.select_for_update().get(id=pk)
        except HelpRequest.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        reason_id = get_param_or_400(request.data, "reasonId", int)

        help_request.status_id = HelpRequestStatus.AllStatus.Canceled
        help_request.cancel_reason_id = reason_id
        help_request.save()
        return Response()

    @action(
        methods=["post"],
        detail=True,
        url_path="finishrequest",
        schema=ManualSchema(
            description="Request owner finishes the request (help executed successfully)",
            fields=[
                coreapi.Field(
                    "id", required=True, location="path", schema=coreschema.Integer()
                )
            ],
        ),
    )
    @transaction.atomic
    def finish_request(self, request: Request, pk):
        # Lock database row to control concurrency in status update
        queryset = self.get_queryset()
        try:
            help_request = queryset.select_for_update().get(id=pk)
        except HelpRequest.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        help_request.status_id = HelpRequestStatus.AllStatus.Finished
        help_request.save()
        return Response()
