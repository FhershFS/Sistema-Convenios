from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):  # pragma: no cover
    def wrapper_func(request, *args, **kwargs):  # pragma: no cover
        if (request.user.is_authenticated):
            return redirect('')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def allowed_users(allowed_roles=[]):  # pragma: no cover
    def decorator(view_func):  # pragma: no cover
        def wrapper_func(request, *args, **kwargs):  # pragma: no cover
            group = None
            print(request.user.groups.exists())
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            else:
                return redirect('/')

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('No tienes autorización para ver esta página.')
        return wrapper_func
    return decorator
