from django.shortcuts import render, redirect, HttpResponse, Http404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout
from .models import Post, Replie, Profile, DailyTask, Plant
from .forms import ProfileForm, PlantForm
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.db.models import Q

# for the forum page
def forum(request):
    # designates user profile
    profile = Profile.objects.all()
    
    # sets html template file
    forum_page = "forum.html"

    if request.method=="POST":   
        user = request.user
        image = request.user.profile.avatar
        content = request.POST.get('content','')
        post = Post(user1=user, post_content=content, image=image)
        post.save()
        alert = True
        return render(request, forum_page, {'alert':alert})
    
    posts = Post.objects.filter().order_by('-timestamp')
    return render(request, forum_page, {'posts':posts})


# for discussion board page
def discussion(request, myid):
    post = Post.objects.filter(id=myid).first()
    replies = Replie.objects.filter(post=post)

    # sets html template file
    discussion_page = "discussion.html"

    # if the user wants to create a new discussion
    if request.method=="POST":
        user = request.user
        image = request.user.profile.avatar
        desc = request.POST.get('desc','')
        post_id = request.POST.get('post_id','')
        reply = Replie(user = user, reply_content = desc, post=post, image=image)
        reply.save()
        alert = True
        return render(request, discussion_page, {'alert':alert})
    
    # otherwise
    return render(request, discussion_page, {'post':post, 'replies':replies})


# for user registration page
def UserRegister(request):

    # variable to take people back to the page
        # will be used to redirect if error in registration
    registerRedirect = '/register'

    # define variables for html template
    login_page = 'login.html'
    register_page = "register.html"

    # if the use wants to create a new profile
    if request.method=="POST":   
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # keep username to less than 15 characters
        if len(username) > 20:
            messages.error(request, "Username must be under 20 characters.")
            return redirect(registerRedirect)
        
        # keep to username to being letters/numbers
        if not username.isalnum():
            messages.error(request, "Username must contain only letters and numbers.")
            return redirect(registerRedirect)
        
        # make sure the confirm passwork matches the password set
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect(registerRedirect)
        
        # check if username has been used before
        try:
            #create user object
            user = User.objects.create_user(username, email, password)

            # define user details
            user.first_name = first_name
            user.last_name = last_name

            # save the user details
            user.save()

            # then take them to the login page
            return render(request, login_page) 
        
        # if the error occurs, inform the user.
        except IntegrityError:
            messages.error(request, "Username already exists. Try again.")
        

    # otherwise keep to page
    return render(request, register_page)


# for use login page
def UserLogin(request):

    # define variables for html template
    login_page = 'login.html'

    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/myprofile")
        else:
            messages.error(request, "Invalid Credentials")
        alert = True
        return render(request, login_page, {'alert':alert})            
    return render(request, login_page)


# for user logout page
def UserLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/login')


# designated login requirement
@login_required(login_url='/login')

# for profile page
@login_required
def myprofile(request):
    profile_page = "profile.html"
    profile_redirect = '/myprofile'

    profile, created = Profile.objects.get_or_create(user=request.user)
    current_week_tasks = []

    # check request type; make sure proper
    if request.method == "POST":
        # set variables commonly used
        avatar_form = ProfileForm(request.POST, request.FILES, instance=profile)
        plant_form = PlantForm(request.POST, request.FILES, instance=profile)

        # if avatar is being changed
        if 'avatar_submit' in request.POST:
            if avatar_form.is_valid():
                avatar_form.save()
                messages.success(request, 'Profile picture updated successfully!')
                return redirect(profile_redirect)

        # if plant is being changed/added
        elif 'plant_submit' in request.POST:
            if plant_form.is_valid():
                plant_form.save()
                messages.success(request, 'Plant information updated successfully!')
                return redirect(profile_redirect)

        # if the plant is being removed
        elif 'remove_plant_image_1' in request.POST:
            profile.plant_image_1 = None
            profile.save()
            messages.success(request, 'Plant image removed successfully!')
            return redirect(profile_redirect)

        # if the watering schedule is being edited
        elif 'daily_tasks_submit' in request.POST:
            for day in range(7):
                task_description = request.POST.get(f'task_{day}', '')

                # default check to unchecked
                completed = request.POST.get(f'completed_{day}', False)
                
                # set checked to on if true
                completed = completed == 'on'
                task_date = calculate_task_date(day)
                daily_task, created = DailyTask.objects.get_or_create(user=request.user, task_date=task_date)
                daily_task.task_description = task_description
                daily_task.completed = completed
                daily_task.save()
            messages.success(request, 'Daily tasks updated successfully!')
            return redirect(profile_redirect)

    # otherwise keep as is
    else:
        avatar_form = ProfileForm(instance=profile)
        plant_form = PlantForm(instance=profile)

        for day in range(7):
            task_date = calculate_task_date(day)
            daily_task, created = DailyTask.objects.get_or_create(user=request.user, task_date=task_date)
            current_week_tasks.append(daily_task)

    # return/render the page
    return render(request, profile_page, {'avatar_form': avatar_form, 'plant_form': plant_form, 'created': created, 'current_week_tasks': current_week_tasks})

##############################################################################
# Search views
##############################################################################
def search(request):
    # sets html template file
    search_page = "search.html"
    
    #defines what happens when there is a POST request
    if request.method == "POST":
        plant = request.POST.get("q")
        search_result = Plant.objects.filter(Q(common_name__icontains=plant) | Q(scientific_name__icontains=plant))
        return render(request, search_page, {'search_result':search_result })

    #defines what happens when there is a GET request
    else:
        return render(request,search_page)


def search_result(request, scientific_name):
    #sets template file
    result_page = "search_result.html"

    plant = Plant.objects.get(scientific_name=scientific_name)

    return render(request, result_page, {'plant':plant })



#################### ADDITIONAL FUNCTIONS

# calculates current date to determine what week needs to be displayed
def calculate_task_date(day):
    from datetime import datetime, timedelta
    today = datetime.today()
    start_of_week = today - timedelta(days=today.weekday())
    task_date = start_of_week + timedelta(days=day)
    return task_date
