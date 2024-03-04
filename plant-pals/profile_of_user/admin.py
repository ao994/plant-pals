# gives support for the django admin site. Accessible with http://wherever_your_terminal_is_hosting/admin
from django.contrib import admin

# register models here.
from .models import Post, Replie, Profile

# make sure to register what you want to be able to have admin control of from models!
# if you don't, you can't access it on the admin site w/ admin control panels
admin.site.register(Post)
admin.site.register(Replie)
admin.site.register(Profile)

#import plants database model
from .models import Plant

admin.site.register(Plant)
