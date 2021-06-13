from django.contrib.auth.models import User
from django.db import models

class CompanyDetail(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    companyname=models.CharField(max_length=50)

    def __str__(self):
        return str(self.user)
