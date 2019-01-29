from django.urls import path
from apps.site_bitcoin.views import home, send, receive, transaction

# Rotas do sistema, send, receive, transaction e a página inicial
urlpatterns = [
    path('', home, name="home"),
    path('send/', send, name="send"),
    path('receive/', receive, name="receive"),
    path('transaction/<slug:hash>/', transaction, name="transaction"),
]
