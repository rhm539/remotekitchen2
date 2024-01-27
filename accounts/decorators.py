from functools import wraps
from django.http import HttpResponseForbidden

def owner_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_owner:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("Permission Denied")
    return _wrapped_view