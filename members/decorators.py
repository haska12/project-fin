from django.http import HttpResponse
from django.shortcuts import redirect
#decorator
def unauthenticated_user(wiew_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        else:
            return wiew_func(request,*args,**kwargs)
    
    return wrapper_func


def  allowed_users(Allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request,*args,**kwargs):
            group =None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
            if group =="admin" or group =="professeure" :
                return view_func(request,*args,**kwargs)
            else:
                return redirect("home")
        return wrapper_func
    return  decorator
