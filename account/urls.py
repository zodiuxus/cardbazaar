from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
app_name="account"
urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("buyeraccount/", views.register_buyer, name="buyeraccount"),
    path("selleraccount/", views.register_seller, name="selleraccount"),
    path("userprofile/", views.user_profile, name="userprofile"),
    path("userprofile/addcard", views.add_seller_card, name="addcard"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
