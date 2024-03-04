# imports from OUR models.py
from .models import Profile

# imports from django
from django import forms

# models.py connects with this!
## model = Profile | tells the code to connect with that specific model made
## fields = [''] | says that the names in the list is now a variable. You
   ## can see these used in models.py in our Profile class.

# profile form draws from profile model and has an avatar image field
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']

# plant form draws from profile model and has plant image fields
class PlantForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['plant_image_1', 'plant_name_1']
        # Add fields for plant_image_2, plant_name_2, and so on...
        # if doing this, make sure to add to models.py
