from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('burkoff/', include('polls.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('social_django.urls')),
    path('admin/', admin.site.urls),
]