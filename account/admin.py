from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import UserAccount, BuyerAccount, SellerAccount, SellerCardDetail

# Register your models here.
class BuyerInline(admin.StackedInline):
    model = BuyerAccount
    can_delete = True

class SellerInline(admin.StackedInline):
    model = SellerAccount
    can_delete = True

class AccountAdmin(UserAdmin):
    list_display = ('username', 'email', 'full_name', 'date_joined', 'last_login', 'is_admin')
    search_fields = ('username', 'email', 'full_name')
    readonly_fields = ('date_joined', 'last_login')
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

    inlines = [BuyerInline, SellerInline]

admin.site.register(UserAccount, AccountAdmin)
admin.site.register(BuyerAccount)
admin.site.register(SellerAccount)
admin.site.register(SellerCardDetail)