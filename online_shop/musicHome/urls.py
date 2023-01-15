from django.urls import path
from .views import *

urlpatterns = [
    path('log_in/', LoginUser.as_view(), name='log_in'),
    path('home/', home, name='home'),
    path('admin_account/', admin_account),
    path('personal_account/', personal_account),
    path('products/', products),
    path('registrate/', RegisterUser.as_view(), name='registrate'),
    path('to_buy/', to_buy),
    #path('products_slag')
]