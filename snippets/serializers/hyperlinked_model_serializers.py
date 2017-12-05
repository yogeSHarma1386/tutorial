from enum import Enum

from django.contrib.auth.models import User
from rest_framework import serializers

from ..models import Snippet


class SerializerPreTextTypes(Enum):
    NORMAL = ''
    VIEW_SET = 'vs-'
    HYPERLINKED = 'h-'

serializer_type_in_use = SerializerPreTextTypes.VIEW_SET.value


class SnippetHyperLinkedSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # This view_name is field-level.
    highlight = serializers.HyperlinkedIdentityField(view_name='{0}snippet-highlight'.format(serializer_type_in_use),
                                                     format='html')

    class Meta:
        model = Snippet
        fields = ('url', 'id', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style')

        # Mentioning serializer-level:view_name explicitly
        extra_kwargs = {
            'url': {'view_name': 'snippet-detail'}
        }


class UserHyperLinkedSerializer(serializers.HyperlinkedModelSerializer):
    # This view_name is field-level.
    snippets = serializers.HyperlinkedRelatedField(many=True,
                                                   view_name='{0}snippet-detail'.format(serializer_type_in_use),
                                                   read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets')

        # Mentioning serializer-level:view_name explicitly
        extra_kwargs = {
            'url': {'view_name': 'user-detail'}
        }
