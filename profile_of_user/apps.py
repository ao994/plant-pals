# django library for app config
from django.apps import AppConfig

# connects everything to our actual app "profile_of_user"
# can add additional apps
class ProfileOfUserConfig(AppConfig):
    name = 'profile_of_user'
