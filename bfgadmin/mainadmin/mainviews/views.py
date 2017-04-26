from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import datetime

@login_required
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
