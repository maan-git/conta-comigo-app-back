from rest_framework import serializers
from help.models.help_request import HelpRequest
from help.models.help_category import HelpCategory
from help.models.help_request_status import HelpRequestStatus
from app.models.user import User
from help.models.helping_status import HelpingStatus
from help.models.helprequest_helpers import HelpRequestHelpers
from help.models.help_request_cancel_reason import HelpRequestCancelReason


class CategorySimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpCategory
        fields = ("id", "description")


class StatusSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpRequestStatus
        fields = ("id", "description")


class CancelReasonSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpRequestCancelReason
        fields = ("id", "description")


class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "first_name", "last_name", "avatar")


class HelpingStatusSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpingStatus
        fields = ("id", "description")


class HelpRequestHelpersSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpRequestHelpers
        fields = ("helper_user", "status")

    helper_user = UserSimpleSerializer()
    status = HelpingStatusSimpleSerializer()


class HelpRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpRequest
        exclude = ("owner_user",)
        depth = 1

    request_user = UserSimpleSerializer(source="owner_user", read_only=True)
    helping_users = serializers.SerializerMethodField()
    category = CategorySimpleSerializer(many=False, read_only=False)
    status = StatusSimpleSerializer(many=False, read_only=True)
    cancel_reason = CancelReasonSimpleSerializer(many=False, read_only=True)
    address_id = serializers.IntegerField()

    def create(self, validated_data):
        validated_data["owner_user"] = self.context["request"].user
        return super().create(validated_data)

    @classmethod
    def get_helping_users(cls, obj: HelpRequest):
        helping_user_relations = HelpRequestHelpers.objects.filter(help_request=obj)

        return HelpRequestHelpersSerializer(helping_user_relations, many=True).data


class HelpRequestSerializerWrite(HelpRequestSerializer):
    category = serializers.PrimaryKeyRelatedField(
        many=False, read_only=False, queryset=HelpCategory.objects.all()
    )
