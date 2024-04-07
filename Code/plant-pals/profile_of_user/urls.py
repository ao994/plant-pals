from django.urls import path
from . import views

urlpatterns = [
    # change first parameter to the file path location
    # the second parameter acesses the function for the paticular action in
       # the views file
    # the last paramter just sets a name for it

    # designates the file path for how they can be found in the website.
    ## Ex: html://our_site/ 
        ## takes us to our forum page because that is currently our home page
    ## Ex: html://our_site/login/
        ## takes us to the login page
    path("", views.forum, name="Forum"),
    path("discussion/<int:myid>/", views.discussion, name="Discussions"),
    path("register/", views.UserRegister, name="Register"),
    path("login/", views.UserLogin, name="Login"),
    path("logout/", views.UserLogout, name="Logout"),
    path("myprofile/", views.myprofile, name="Myprofile"),
    path("search/", views.search, name="Search"),
]
