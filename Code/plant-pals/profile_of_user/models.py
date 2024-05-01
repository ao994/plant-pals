from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.db.models import UniqueConstraint # Constrains fields to unique values

# profile model
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, unique = True, on_delete=models.CASCADE)    
    # for user avatar images
    avatar = models.ImageField(upload_to="images", default="images/user.png")

    ## for the plants. If more portfolio plants are wanted, copy and past this
        ## just remember to change the name, add it to the PlantForm class in forms.py,
        ## adjust views.py to allow for another plant submission, and add it to
        ## the profile html page.

    # change default to a temp plant when we have one
    plant_image_1 = models.ImageField(upload_to="additional_images", default="images/user.png")
    plant_name_1 = models.CharField(max_length=60,  default="")

    #makes sure the images are deleted when a profile is deleted
    def delete(self, using=None, keep_parents=False):
        self.avatar.delete()
        self.plant_image_1.delete()
        super().delete()

# post model
class Post(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    post_id = models.AutoField
    post_content = models.CharField(max_length=5000)
    timestamp= models.DateTimeField(default=now)
    image = models.ImageField(upload_to="images",default="")

    #makes sure the image is deleted when a post is deleted
    def delete(self, using=None, keep_parents=False):
        self.image.delete()
        super().delete()

# reply model (associated with post)
class Replie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    reply_id = models.AutoField
    reply_content = models.CharField(max_length=5000) 
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default='')
    timestamp= models.DateTimeField(default=now)
    image = models.ImageField(upload_to="images",default="")

    # makes sure the image is deleted when a reply is deleted
    def delete(self, using=None, keep_parents=False):
        self.image.delete()
        super().delete()

### model for plant watering schedule
class DailyTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_date = models.DateField()
    task_description = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'task_date')

##############################################################################
# Plant data entry model
##############################################################################
class Plant(models.Model):
    """This model is for entering plants into the database."""

    #Fields
    scientific_name = models.CharField("scientific name", max_length = 100, unique = True)
    common_name = models.CharField("common name", max_length = 50)
    growth_habit = models.CharField("growth habit", max_length = 20)
    duration = models.CharField("seasonal duration", max_length = 20)
    sun_requirements = models.CharField("sun requirements", max_length = 20)
    water = models.CharField("water recommended", max_length = 50)
    temp_low_F = models.FloatField("lowest temperature (F)", max_length = 5)
    temp_high_F = models.FloatField("highest temperature (F)", max_length = 5)
    image = models.ImageField("plant image", upload_to="plant_database",default="")

    #ordering of plants
    class Meta:
        ordering = ['scientific_name']

    #methods
    def __str__(self):
        return self.scientific_name
    
    #makes sure the image is deleted when a plant is deleted
    def delete(self, using=None, keep_parents=False):
        self.image.delete()
        super().delete()
