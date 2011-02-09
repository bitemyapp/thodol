def notification(request):
    status = "notifyinactive"
    """
    # leaving this for later
    if request.user:
        status = "notifyactive"
    """
    return {'notify':status}
