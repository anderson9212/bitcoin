from django.urls import path
from apps.site_bitcoin.views import home, send_email, send, receive, transaction

urlpatterns = [
    path('', home, name="home"),
    path('send_email/', send_email, name="send_email"),
    path('send/', send, name="send"),
    path('receive/', receive, name="receive"),
    path('transaction/<slug:hash>/', transaction, name="transaction"),
]
