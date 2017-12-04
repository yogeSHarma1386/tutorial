from . import function_based, class_based, mixin_based

# Step1
func_snippet_detail = function_based.snippet_detail
func_snippet_list = function_based.snippet_list

# Step2
klass_snippet_detail = class_based.SnippetList.as_view()
klass_snippet_list = class_based.SnippetDetail.as_view()

# Step3
mixin_snippet_detail = mixin_based.SnippetDetail.as_view()
mixin_snippet_list = mixin_based.SnippetList.as_view()
