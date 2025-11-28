from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, password, email=None):
        if not username:
            username = 'username'
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, email=None):
        if not username:
            username = 'username'

        user = self.create_user(username, password, email)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
