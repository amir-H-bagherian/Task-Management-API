from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError("Email is required!")
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)
        
        if not kwargs.get('is_staff'):
            raise ValueError("is_staff must be True for superuser")
        if not kwargs.get('is_superuser'):
            raise ValueError("is_superuser must be True for superuser")
        return self.create_user(email, password, **kwargs)