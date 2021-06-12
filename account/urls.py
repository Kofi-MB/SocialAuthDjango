from . import views
from django.urls import path

urlpatterns = [
    path('',views.test),
    path('get-user',views.get_user),
    path('send-sms',views.send_sms)
]