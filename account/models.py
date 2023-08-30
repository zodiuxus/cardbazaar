import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings

# Create your models here.
class UserAccountManager(BaseUserManager):
    def create_user(self, email, username, full_name, password=None):
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            full_name = full_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, full_name, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username = username,
            full_name = full_name,
            password=password
        )
        
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True

        user.save(using=self._db)
        return user

class UserAccount(AbstractBaseUser):
    uuid = models.UUIDField(verbose_name="user uuid", primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(verbose_name="email", max_length=250, blank=False)
    username = models.CharField(max_length=30, blank=False, unique=True)    
    full_name = models.CharField(max_length=50, blank=False)
    phone = models.IntegerField(blank=True, null=True) 
    date_joined = models.DateTimeField(verbose_name="date of join", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login time", auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'full_name', ]

    objects = UserAccountManager()        

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
    
class BuyerAccount(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    shipping_address = models.CharField(max_length=250)
    billing_address = models.CharField(max_length=250)
    def __str__(self):
        return self.user.username
    
class SellerAccount(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    swift_code_transaction = models.CharField(max_length=30)
    seller_reputation = models.DecimalField(decimal_places=2, max_digits=3)
    def __str__(self):
        return self.user.username

def user_dir_upload(instance, filename):
    return "user_{0}/{1}".format(instance.seller_details, filename)

class SellerCardDetail(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    card_name = models.TextField(default="CARDNAME")
    card_quality = models.CharField(max_length=16)
    card_price = models.DecimalField(max_digits=19, decimal_places=2)
    card_image = models.ImageField(verbose_name="OPTIONAL, card images do not need to be supplied, but sellers are encouraged to do so.", blank=True, upload_to=user_dir_upload)
    card_url = models.URLField()
    card_notes = models.TextField(blank=True)
    card_stock = models.IntegerField(default=0, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)
    seller_details = models.ForeignKey(SellerAccount, on_delete=models.CASCADE)
    def __str__(self):
        return self.seller_details.user.username
    