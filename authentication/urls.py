from .views import *
from django.urls import path
urlpatterns = [

    path('', home,name="home"),
    path('signup',Signup.as_view(),name="signup"),
    path('login',user_login,name="login"),
    path('dashboard',dashboard, name="dashboard"),
    path('withdrow',WithDraw, name="withdrow"),
    path('topup',TopUp,name="topup"),
    path('logout',User_Logout,name="logout"),
    path('send',Send,name="send"),
    path('invoicing',Invoicing,name="invoicing"),
    path("utilities",Utilities,name="utilities"),
    
    path("reports", Reports, name="reports"),
    path("userprofile",User_Profile, name="userprofile"),

]
