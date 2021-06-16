from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class StudentUser(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    mobile = models.CharField(max_length = 15, null=True)
    type = models.CharField(max_length = 15, null=True)
    def _str_(self):
        return self.user.username

class JobPost(models.Model):
    company = models.CharField(max_length = 100, null=True)
    jobdescription = models.CharField(max_length = 100, null=True)
    vaccany = models.IntegerField()

class applyjob(models.Model):
    name = models.CharField(max_length = 100, null=True)
    email_id = models.EmailField()
    document = models.FileField()
    


