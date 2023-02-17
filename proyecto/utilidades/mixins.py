from django.core.exceptions import PermissionDenied

class IsAdminMixins:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.es_admin:
            raise PermissionDenied
        return super(IsAdminMixins, self).dispatch(request, *args, **kwargs)
    
def is_admin_required():
    def permisos_requeridos(f):
        def check(request, *arg, **kwargs):
            if request.user.is_authenticated and not request.user.es_admin:
                raise PermissionDenied
            return f(request, *arg, **kwargs)
        return check
    return permisos_requeridos