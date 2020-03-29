from rest_framework import serializers
from help.models.help_request import HelpRequest
from help.models.help_category import HelpCategory
from app.models.user import User
from help.models.helping_status import HelpingStatus
from help.models.helprequest_helpers import HelpRequestHelpers


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
