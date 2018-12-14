from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('page/<int:page_number>/', views.posts_list, name='posts_list'),
    path('categories/', views.categories, name='categories'),
    path('categories/<int:category_id>/', views.category, name='category'),
    path('post/<int:id>/', views.post, name='post'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),
]
