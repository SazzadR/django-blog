from django.urls import path
from accounts.views.register import Register
from accounts.views.login import Login, Logout

app_name = 'accounts'

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout')
]
