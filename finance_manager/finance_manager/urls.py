from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('finance/', include('personal_finance.urls')),
    path('lending/', include('peer_to_peer_lending.urls')),
]
