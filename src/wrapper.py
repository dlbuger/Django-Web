from django.shortcuts import HttpResponse

def allowed_users(allow = []):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                for group in request.user.groups.all():
                    if group.name in allow:
                        return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("没有权限")
        return wrapper_func
    return decorator