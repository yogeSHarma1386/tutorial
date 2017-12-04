from .class_based import *
from .function_based import snippet_detail as func_snippet_detail, snippet_list as func_snippet_list

snippet_detail = SnippetDetail.as_view()
snippet_list = SnippetList.as_view()