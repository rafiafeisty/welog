
from django.contrib import admin
from django.urls import path, include
from .import views

app_name="login"
urlpatterns = [
path('admin/', admin.site.urls),
path('', views.login, name='login'),
path('checking/', views.checking, name='checking'),
path('allblog/', include('allblog.urls')),
]
