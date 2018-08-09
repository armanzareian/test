from django.urls import path
# from first_app.views import user
from first_app.views import register,user_login

app_name="first_app"

urlpatterns=[
     path("register/",register,name="register"),
    path("login/",user_login,name="login"),

]
