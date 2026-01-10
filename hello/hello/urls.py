from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include('helloworld.urls')),
    path('tasks/', include('tasks.urls', namespace='tasks')),
    path('challenges/', include('challenges.urls')),
]
