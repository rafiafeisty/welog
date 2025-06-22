
from django.contrib import admin
from django.urls import path, include
from .import views

app_name="signup"
urlpatterns = [
path('admin/', admin.site.urls),
path('', views.signup, name='Signup'),
path('saving/', views.saving, name='saving'),
path('login/', include('login.urls')),
]
