from django.urls import path
from App_Login import views

app_name = "user"

urlpatterns = [
    path('',views.user,name='user'),
    path('register/',views.register,name='register'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
]
