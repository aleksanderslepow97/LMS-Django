from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('lms.urls'), name='lms'),
    path('users/', include('users.urls'), name='users'),
]
