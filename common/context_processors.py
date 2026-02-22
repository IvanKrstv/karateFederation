from common.forms import SearchForm

def search_form_context_processor(request):
    return {
        'search_form': SearchForm(request.GET or None)
    }
