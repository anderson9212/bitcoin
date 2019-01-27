from django.urls import path, include

urlpatterns = [
    path('', include('apps.site_bitcoin.urls')),
]
