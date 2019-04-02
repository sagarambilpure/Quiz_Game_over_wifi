from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path("",views.index, name="index"),
    path("loggedout",views.log_me_out, name="logout"),
    path("home",views.home,name="home"),
    path("login",views.my_login,name="authenticateuser"),
    path("register",views.register,name="register"),
    path("signup",views.signup,name="gamerregister"),
    path("question",views.question,name="question"),
    path("answersubmit",views.answersubmit,name="answersubmit"),
]
