from rest_framework import renderers, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from . import function_based, class_based, mixin_based, generic_api_view_based, hyperlinked_generic_api_view_based as h_generic
from ..models import Snippet

################################ Snippet Serializers ################################
# Step1
func_snippet_detail = function_based.snippet_detail
func_snippet_list = function_based.snippet_list

# Step2
klass_snippet_detail = class_based.SnippetDetail.as_view()
klass_snippet_list = class_based.SnippetList.as_view()

# Step3
mixin_snippet_detail = mixin_based.SnippetDetail.as_view()
mixin_snippet_list = mixin_based.SnippetList.as_view()

# Step4
generic_api_view_snippet_detail = generic_api_view_based.SnippetDetail.as_view()
generic_api_view_snippet_list = generic_api_view_based.SnippetList.as_view()


################################## User Serializers ##################################

generic_api_view_user_detail = generic_api_view_based.UserDetail.as_view()
generic_api_view_user_list = generic_api_view_based.UserList.as_view()


############################### HyperLinked Serializers ###############################
h_generic_api_view_snippet_detail = h_generic.SnippetHyperLinkedDetail.as_view()
h_generic_api_view_snippet_list = h_generic.SnippetHyperLinkedList.as_view()

h_generic_api_view_user_detail = h_generic.UserHyperLinkedDetail.as_view()
h_generic_api_view_user_list = h_generic.UserHyperLinkedList.as_view()


################################## Entry Point ##################################
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format),

        'h-users': reverse('h-user-list', request=request, format=format),
        'h-snippets': reverse('h-snippet-list', request=request, format=format)
    })


class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)
