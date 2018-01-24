from enum import Enum

from django.contrib.auth.models import User
from rest_framework import serializers

from tutorial.utils import AppNameSpace
from ..models import Snippet


snippet_namespace = AppNameSpace.REST.value
snippet_namespace_usage = snippet_namespace + ':'


class SerializerPreTextTypes(Enum):
    NORMAL = snippet_namespace_usage + ''
    VIEW_SET = snippet_namespace_usage + 'vs-'
    HYPERLINKED = snippet_namespace_usage + 'h-'
    ROUTED_VIEW_SET = snippet_namespace_usage + 'r-vs-'


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
            'url': {'view_name': '{0}snippet-detail'.format(SerializerPreTextTypes.NORMAL.value)}
        }


class UserHyperLinkedSerializer(serializers.HyperlinkedModelSerializer):
    # This view_name is field-level.
    snippets = serializers.HyperlinkedRelatedField(many=True,
                                                   view_name='{0}snippet-detail'.format(serializer_type_in_use),
                                                   read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'rest')

        # Mentioning serializer-level:view_name explicitly
        extra_kwargs = {
            'url': {'view_name': '{0}user-detail'.format(SerializerPreTextTypes.NORMAL.value)}
        }
