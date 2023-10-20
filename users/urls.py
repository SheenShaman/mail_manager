from django.urls import path

from users.apps import UsersConfig
from users.views import LoginView, LogoutView, RegisterView, ProfileView, ProfileDeleteView, gen_password, verify

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/delete/<int:pk>', ProfileDeleteView.as_view(), name='profile_delete'),
    path('profile/gen_password/', gen_password, name='gen_password'),
    path('verify/<code>/', verify, name='verify_email'),
]
