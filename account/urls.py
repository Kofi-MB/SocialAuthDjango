from . import views
from django.urls import path

urlpatterns = [
    path('ldaccessToken',views.ldaccessToken),
    path('get-user',views.get_user),
    path('setcompany',views.setcompany),
    path('send-sms',views.send_sms)
]