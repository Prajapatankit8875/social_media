from django.contrib import admin
from django.urls import path
from userauth import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('signup/',views.signup),
    path('login/',views.login), 
    path('logout/',views.logout),
]