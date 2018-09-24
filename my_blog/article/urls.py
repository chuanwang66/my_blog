from django.urls import path

from . import views

# 正在部署的应用的名称
app_name = 'article'

urlpatterns = [
    path('hello_world/', views.hello_world, name='hello_world'),
    path('hello_world2/', views.hello_world2, name='hello_world2'),
    path('article_list/', views.article_list, name='article_list'),
]
