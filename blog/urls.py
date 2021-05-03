from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('post/',views.ListPageView.as_view(), name = 'index'),
    path('', views.AboutUs.as_view() , name = 'about'),
    path('post/create/', views.CreatePageView.as_view() , name = 'post_create'),
    path('post/register/', views.Register.as_view() , name = 'register'),
    path('post/<pk>/comment/', views.add_comment_to_post , name = 'post_comment'),
    path('post/<pk>/detail/', views.DetailPageView.as_view() , name = 'post_detail'),
    path('post/<pk>/delete/', views.DeletePageView.as_view() , name = 'post_delete'),
    path('post/<pk>/edit/', views.UpdatePageView.as_view() , name = 'post_edit'),
    path('password_change/', views.PasswordChangeViewPage.as_view() , name = 'password_change')

]
