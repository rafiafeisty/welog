
from django.contrib import admin
from django.urls import path, include
from .import views

app_name='allblog'
urlpatterns = [
path('admin/', admin.site.urls),
path('', views.index, name='index'),
path('myblog/', views.myblog, name='myblog'),
path('myblog/details/<int:blog_id>/', views.details, name='details'),
path('madeblog/', views.madeblog, name='madeblog'),
path('details/<int:blog_id>/', views.details, name='details'),
path('forminput/', views.forminput, name='forminput'),
path('commentsaving/', views.commentsaving, name='commentsaving'),
path('myblog/edit/<int:blog_id_to_edit>/', views.edit, name='edit'),
path('myblog/delete/<int:blog_id_to_edit>/', views.delete, name='delete'),
path('formedit/<int:blog_id_to_edit>/', views.formedit, name='formedit'),
]
