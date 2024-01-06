from django.contrib import admin
from django.urls import path, include
from wikinformation.views import bot, sendmail


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('wikinformation.urls')),
    path('bot/',bot),
    path('mail/', sendmail),
]