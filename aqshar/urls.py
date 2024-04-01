from django.contrib import admin
from django.urls import path, include
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("core/", include("core.urls")),
    path("chat/", views.chat, name="chat"),
    path("login/", views.login_user, name="login"),
    path("catalog/", views.catalogue, name="catalog"),
    path("signup/", views.signup, name="signup"),
    path("checkout/", views.checkout, name="checkout"),
    path("donate/", views.donating, name="donating"),
    path("sell/", views.selling, name="selling"),
    path("account/", views.account, name="account"),
    path("orders/", views.orders, name="orders"),  # Added trailing slash
    path("admin/", admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
