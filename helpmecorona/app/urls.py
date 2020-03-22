from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /post/5/
    path('detail/<int:post_id>/', views.detail, name='detail'),
    path('help/<int:post_id>/', views.help, name='help'),
]
