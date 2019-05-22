from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from allauth.socialaccount.models import SocialAccount
import json
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="user/",null=True,blank=True)
    is_private = models.BooleanField(default=False)
    def image_url(self):
        sUser=SocialAccount.objects.filter(user=self.user)
        if self.image:
            return self.image.url
        elif sUser.exists():
            if sUser[0].provider=='facebook':
                return "http://graph.facebook.com/"+sUser[0].uid+"/picture?type=large"
            elif sUser[0].provider=='google':
                profile = json.dumps(sUser[0].extra_data)
                profile=json.loads(profile)
                return profile['picture']
        else:
            return None

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()