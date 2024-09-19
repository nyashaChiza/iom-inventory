from django.contrib import admin
from django.urls import path, include  # Import include

urlpatterns = [
    path('optimus/', admin.site.urls),
    path('stock/', include('stock.urls')), 
    path('accounts/', include('accounts.urls')), 
]