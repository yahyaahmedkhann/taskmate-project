from django.urls import path
from users_app import views 
from django.contrib.auth import views as auth_views
from .views import CustomLogout

# class CustomLogoutView(LogoutView):
#     http_method_names = ['get', 'post']

urlpatterns = [
    path('register', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    
    path('logout/',CustomLogout, name='logout')
  
]

