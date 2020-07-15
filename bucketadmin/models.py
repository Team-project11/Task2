from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

# Create your models here.
class Funpost(models.Model):
    Img_post = models.FileField(blank=True,null=True,upload_to='img')
    Description = models.CharField(max_length=500)
    user = models.ForeignKey(User,blank=True,on_delete=models.CASCADE,null=True )


status = [
    ('Like','Like'),
    ('Dislike','Dislike'),
]
class Funstatus(models.Model):
    Status = models.CharField(choices=status,max_length=100)
    user_posted = models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name='user_posted2user_posted' )
    user = models.ManyToManyField(User)
    def __str__(self):
        return self.Status

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
    