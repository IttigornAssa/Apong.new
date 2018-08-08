from django.db import models

# Create your models here.
class MOU(models.Model):
    title = models.CharField(max_length=500)
    start_date = models.DateField()
    expire_date = models.DateField()
    tpye = models.CharField(max_length=500)
    contact = models.CharField(max_length=500,blank=True,null=True)
    url = models.CharField(max_length=500,blank=True,null=True)

class Student(models.Model):
    name = models.CharField(max_length=500)
    image=models.ImageField(upload_to='images',default='\images\icon-user-default.png')
    des = models.CharField(max_length=500,null=True)
    def __unicode__(self):
        return u"%s"%(self.name)
