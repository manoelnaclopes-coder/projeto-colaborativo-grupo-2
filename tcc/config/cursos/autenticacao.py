from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class EmailBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        
        User = get_user_model()
        
        email = username or kwargs.get('email')
        
        if not email or not password:
            return None
        

        usuarios = User.objects.filter(email__iexact=email)

        if usuarios.count() != 1:
            return None

        usuario = usuarios.first()

        

        if usuario.check_password(password):
            return usuario

        return None