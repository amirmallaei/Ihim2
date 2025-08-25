from django.urls import path
from user.views import (RegisterView, ActiveUserView, LoginView,
                        LogoutView)

app_name = "user"

urlpatterns = [
    path('signup/', RegisterView.as_view(), name="signup"),
    path('activate/<str:token>/', ActiveUserView.as_view(), name="activate"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(),name='logout')
  
]