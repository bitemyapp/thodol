from thodol import settings

def notification(request):
    status = "notifyinactive"
    """
    # leaving this for later
    if request.user:
        status = "notifyactive"
    """
    return {'notify':status}

def site_title(request):
    try:
        site_title = settings.SITE_TITLE
    except:
        site_title = None
    return {"site_title":site_title}
