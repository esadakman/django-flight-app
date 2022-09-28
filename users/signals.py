from django.contrib.auth.models import User
from django.db.models import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# kullanıcı kayıt olduğunda login olmasını ve token oluşturmayı sağlamak için signals dosyası oluşturduk
@receiver(post_save, sender=User)
def create_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)