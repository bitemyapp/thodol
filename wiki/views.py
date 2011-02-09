# wheeeeee
from django.views.generic.simple import direct_to_template
from django.shortcuts import get_object_or_404
from wiki.models import Page, get_or_none
from django.contrib.auth.decorators import login_required

"""
style = request.COOKIES.get('style')
highlightstyle = request.COOKIES.get('highlightstyle')
if not highlightstyle:
    highlightstyle = "shThemeRDark"
# eldritch bullshit, don't ask.
"""
def index(request):
    pages = Page.objects.order_by('-last_changed')[:50]
    return direct_to_template(request, 'wiki/index.html', locals())

def page_view(request, slug):
    page = get_or_none(Page, slug=slug)
    if not page:
        # Don't tell me this isn't good. I know it isn't good.
        deslug = slug.replace('-', ' ')
    return direct_to_template(request, 'wiki/page_view.html', locals())

def page_history(request, slug):
    page = get_object_or_404(Page, slug=slug)
    records = page.record_set.order_by('-last_changed')[:2]
    return direct_to_template(request, 'wiki/page_history.html', locals())

@login_required
def page_edit(request, slug):
    page = get_or_none(Page, slug=slug)
    if not page:
        title = slug.replace('-', ' ')
    else:
        title = page.name
    if request.method == "POST":
        new_content = request.POST.get('edit')
        if page:
            page.content = new_content
            page.save()
        else:
            page = Page(name=title, content=new_content, slug=slug)
            page.save()
    return direct_to_template(request, 'wiki/page_edit.html', locals())
