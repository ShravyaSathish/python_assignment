from django.contrib.auth.base_user import BaseUserManager
# from .generateToken import generateToken

class UserManger(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is not valid') 
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)


        if extra_fields.get('is_staff') is not True:
            raise ValueError(('must be a staff'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(('must be super user'))
        user =  self.create_user(email, password, **extra_fields)
        return user
    



