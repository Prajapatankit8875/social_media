from django.contrib import admin
from django.urls import path
from userauth import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'), 
    path('logout/',views.logout,name='logout'),
    path('upload/',views.upload,name='upload'),
    path('like-post/<str:id>',views.likes,name='like_post'),
    path('#<str:id>',views.home_posts),
]