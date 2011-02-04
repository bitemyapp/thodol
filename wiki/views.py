# wheeeeee
from django.views.generic.simple import direct_to_template

def index(request):
    style = request.COOKIES.get('style')
    highlightstyle = request.COOKIES.get('highlightstyle')
    if not highlightstyle:
        highlightstyle = "shThemeRDark"
    return direct_to_template(request, 'wiki/index.html', locals())