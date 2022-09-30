from rest_framework import permissions

# ! flightların sadece yetkili kişiler tarafından oluşturulması ve değiştirilmesi için permission.py dosyasını oluşturduk ⬇️
class IsStafforReadOnly(permissions.IsAdminUser):
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)

# ? oluşturduğumuz permisson'ı views.py'a gidip import ediyoruz