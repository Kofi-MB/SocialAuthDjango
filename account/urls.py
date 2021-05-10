from . import views
from django.urls import path

urlpatterns = [
    path('get-user',views.get_user),
    path('send-sms',views.send_sms)
]