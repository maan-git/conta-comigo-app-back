from rest_framework import serializers
from help.models.help_request import HelpRequest
from help.models.help_category import HelpCategory
from app.models.user import User
from help.models.helping_status import HelpingStatus
from help.models.helprequest_helpers import HelpRequestHelpers
from help.models.help_request_status import HelpRequestStatus

from utils.views_utils import get_param_or_400
from rest_framework.exceptions import ParseError
from rest_framework import status


class CategorySimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpCategory
        fields = ('id', 'description')


class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name')


class HelpingStatusSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpingStatus
        fields = ('id', 'description')


class HelpRequestHelpersSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpRequestHelpers
        fields = ('helper_user', 'status')

    helper_user = UserSimpleSerializer()
    status = HelpingStatusSimpleSerializer()


class HelpRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpRequest
        exclude = ('owner_user', 'status',)
        depth = 1

    request_user = UserSimpleSerializer(source='owner_user', read_only=True)
    helping_users = serializers.SerializerMethodField()
    category = CategorySimpleSerializer(many=False, read_only=False)

    def create(self, validated_data):
        validated_data['owner_user'] = self.context['request'].user
        return super().create(validated_data)

    def get_helping_users(self, obj: HelpRequest):
        helping_user_relations = HelpRequestHelpers.objects.filter(help_request=obj)

        return HelpRequestHelpersSerializer(helping_user_relations, many=True).data


class HelpRequestSerializerWrite(HelpRequestSerializer):
    category = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=HelpCategory.objects.all())


class HelpStatusRequestSerializer(serializers.ModelSerializer):

    def update_help_status(self, request):
        help_request = self.get_object()
        status_id = get_param_or_400(request.data, 'status_id', int)

        helping_user_help_relation = self._validate_user_help_relation(request)

        if helping_user_help_relation.status_id == HelpRequestStatus.AllStatus.Created and \
                status_id == HelpRequestStatus.AllStatus.Canceled:
            helping_user_help_relation.status_id = HelpRequestStatus.AllStatus.Canceled
            helping_user_help_relation.save()

        elif helping_user_help_relation.status_id == HelpRequestStatus.AllStatus.InProgress and \
                (status_id == HelpRequestStatus.AllStatus.Canceled or \
                 status_id == HelpRequestStatus.AllStatus.Finished):
            helping_user_help_relation.status_id = list(filter(lambda x: request['status_id'] == x,
                                                               HelpRequestStatus.AllStatus))[0]
            helping_user_help_relation.save()
        else:
            raise ParseError(detail=('You cannot make this operation'),
                             code=status.HTTP_400_BAD_REQUEST)

    def _validate_user_help_relation(self, request):
        helping_user_help_relation = HelpRequest.objects.filter(owner_user=request.user).first()
        if not helping_user_help_relation:
            raise ParseError(detail=_('You are not owner of this post'),
                             code=status.HTTP_400_BAD_REQUEST)
        return helping_user_help_relation
