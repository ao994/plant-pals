from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# profile model
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)    
    # for user avatar images
    avatar = models.ImageField(upload_to="images", default="default/user.png")

    ## for the plants. If more portfolio plants are wanted, copy and past this
        ## just remember to change the name, add it to the PlantForm class in forms.py,
        ## adjust views.py to allow for another plant submission, and add it to
        ## the profile html page.

    # change default to a temp plant when we have one
    plant_image_1 = models.ImageField(upload_to="additional_images", default="default/user.png")
    plant_name_1 = models.CharField(max_length=60,  default="")

# post model
class Post(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    post_id = models.AutoField
    post_content = models.CharField(max_length=5000)
    timestamp= models.DateTimeField(default=now)
    image = models.ImageField(upload_to="images",default="")

# reply model (associated with post)
class Replie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    reply_id = models.AutoField
    reply_content = models.CharField(max_length=5000) 
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default='')
    timestamp= models.DateTimeField(default=now)
    image = models.ImageField(upload_to="images",default="")


    


