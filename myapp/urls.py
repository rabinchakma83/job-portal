

from django.urls import path
from myapp.views import Login, home,register       

urlpatterns = [
    
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', Login, name='login'),
]
