# https://127.0.0.1:8000/blog/
# https://127.0.0.1:8000/blog/categories
# https://127.0.0.1:8000/blog/categories/1

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('contacts/', views.contacts_page, name='contacts'),
    path('about/', views.about_page, name='about'),
    path('categories/<int:pk>/', views.category_page, name='category'),
    path('posts/<str:pk>/', views.post_detail, name='post_detail'),
    path('login/', views.login_page, name='login'),
    path('registration/', views.registration_page, name='registration'),
    path('logout/', views.user_logout, name='logout'),
    path('article_form/', views.create_article_view, name='create'),
    path('delete_post/<int:pk>/', views.delete_post, name='delete'),
    path('update/<int:pk>/', views.PostUpdateView.as_view(), name='update'),
    path('search/', views.Search, name='search'),
    path('vote/<int:post_id>/<str:action>/', views.add_vote, name='add_vote'),
]