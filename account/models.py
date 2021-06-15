from django.contrib.auth.models import User
from django.db import models


class CustomAuth(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    mobile_number=models.CharField(max_length=12,unique=True)
    otp=models.CharField(max_length=6)

    def __str__(self):
        return str(self.user)


class CompanyDetail(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=50,blank=True,null=True)
    email=models.CharField(max_length=50,blank=True,null=True)
    companyname=models.CharField(max_length=50)

    def __str__(self):
        return str(self.user)


