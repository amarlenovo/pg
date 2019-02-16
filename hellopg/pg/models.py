from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from PIL import Image

# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic=models.ImageField(default='default.jpg',upload_to='profile_pics')
    def __str__(self):
        return f'{self.user.username} Profile'
    def save(self,*args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img=Image.open(self.profile_pic.path)
        if img.height>125 or img.width>125:
            output_size=(125,125)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)


class UploadPG(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='upload')
    LOCATION_CHOICES=(('pginkhrar','PG In Khrar'),('pgaroundkhrar','PG Around Khrar'))
    location=models.CharField(max_length=15,choices=LOCATION_CHOICES,default='pginkhrar')
    pgname=models.CharField(max_length=150)
    pgtype=models.CharField(max_length=150)
    pglocation=models.CharField(max_length=256)
    pgdescription=models.CharField(max_length=500)
    pgprice=models.IntegerField()
    pgcondition=models.CharField(max_length=150 )
    pgmeals=models.CharField(max_length=256)
    ownername=models.CharField(max_length=50)
    pgmobile=models.BigIntegerField()
    ammenities1=models.CharField(max_length=100)
    ammenities2=models.CharField(max_length=100)
    ammenities3=models.CharField(max_length=100)
    ammenities4=models.CharField(max_length=100)
    ammenities5=models.CharField(max_length=100)
    ammenities6=models.CharField(max_length=100,blank=True,null=True)
    ammenities7=models.CharField(max_length=100,blank=True,null=True)
    ammenities8=models.CharField(max_length=100,blank=True,null=True)
    ammenities9=models.CharField(max_length=100,blank=True,null=True)
    ammenities10=models.CharField(max_length=100,blank=True,null=True,default=' ')
    pgimage1=models.ImageField(upload_to='images')
    pgimage2=models.ImageField(upload_to='images', blank=True,null=True)
    pgimage3=models.ImageField(upload_to='images', blank=True,null=True)

    def __str__(self):
        return self.pgtype
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})
