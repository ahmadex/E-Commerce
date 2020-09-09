from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'my_app'

urlpatterns = [

    path('', views.home, name='home'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('post/<str:pk>', views.post_detail, name='post_detail'),
    path('createpost', views.NewPost.as_view(), name='new_post'),
    path('post_delete/<str:pk>', views.post_delete, name='post_delete'),
    path('post_update/<str:pk>', views.post_update, name='post_update'),
    path('post_publish/<str:pk>', views.post_publish, name='post_publish'),
    path('add_comment/<str:pk>', views.add_comment_to_post, name='add_comment'),
    path('comment_approve/<str:pk>', views.comment_approve, name='comment_approve'),
    path('comment_remove/<str:pk>', views.comment_remove, name='comment_remove'),
    path('draftlist', views.draftlist, name='draftlist'),
    path('login',auth_views.LoginView.as_view(template_name='my_app/login.html'), name='login'),
    path('logout',auth_views.LogoutView.as_view(),name='logout'),

]
