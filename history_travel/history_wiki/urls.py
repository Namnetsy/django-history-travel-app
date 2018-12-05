from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('page/<int:page_number>/', views.posts_list, name='posts_list'),
    path('categories/', views.categories, name='categories'),
    path('categories/<int:category_id>/', views.category, name='category'),
]
