from django.urls import path
from . import views


app_name = 'news'

urlpatterns = [
    path('create/', views.post_create, name='create'),
    path('category/<str:category>/', views.post_by_category, name='post_by_category'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail')
]