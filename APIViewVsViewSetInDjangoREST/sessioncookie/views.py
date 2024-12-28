from django.http import HttpResponse
from django.template import Template, Context
from django.views.decorators.cache import never_cache

@never_cache
def sessionvisit_view(request):
    # Get the current value of 'n_visits' or initialize it to 0
    n_visits = int(request.session.get('n_visits', 0)) + 1
    request.session['n_visits'] = n_visits  # Update the session value

    # Prepare the response
    t = Template('<h1>Total visits: {{ n_visits }}</h1>')
    c = Context({"n_visits": n_visits})  # Use the updated value
    return HttpResponse(t.render(c))


# source:
# https://awstip.com/django-sessions-70a40aaeaa28