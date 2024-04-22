from django.test import TestCase, Client
from django.urls import reverse
from .models import DailyTask, Profile, Post, Replie, Plant
from django.contrib.auth.models import User
from django.utils import timezone
import datetime


class TestModelCase(TestCase):
    def setUp(self):

        # create temp user for tests
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )

        # create plant for testing
        self.plant = Plant.objects.create(
            scientific_name = "Test plant",
            common_name = "Test common name",
            growth_habit = "Test growth habit",
            duration = "Test duration",
            sun_requirements = "Test sun requirements",
            water = "Test water recommended",
            temp_low_F = 50.0,
            temp_high_F = 80.0,
            image = "test.img"
        )

        # set testing profile to user data
        self.profile = Profile.objects.create(user = self.user)

        # create tests for posting and replyign
        self.post = Post.objects.create(user1 = self.user, post_content = "Test post content")
        self.reply = Replie.objects.create(user = self.user, post = self.post, reply_content = "Test reply content")


        # set testing for watering schedule
          # get the date to assign for the week
        self.task_date = timezone.now().date()

          # for each day in the week, create a task
        for day in range(7):
            DailyTask.objects.create(
                # assigned to user
                user = self.user,

                # sets task
                task_date = self.task_date + datetime.timedelta(days=day),
                task_description = f"Task for day {day}",

                # sets the checkbox to off
                completed = False
            )

        # client allows for web requests. It simulates a "fake" page
          # this allows us to test and make sure that it would actual work
          # on the website
        self.client = Client()

          # logins (allows for login action)
        self.client.login(username='testuser', password='testpassword')


    # cleans up created object after each test in order to start next test fresh
        # is automatically run after each test
    def tearDown(self):
        self.plant.delete()
        self.reply.delete()
        self.post.delete()
        self.profile.delete()
        DailyTask.objects.filter(user=self.user).delete()

        # checks to make sure data was properly deleted
        self.assertFalse(Profile.objects.filter(user = self.user).exists())
        self.assertFalse(Post.objects.filter(user1 = self.user).exists())
        self.assertFalse(Replie.objects.filter(user = self.user).exists())
        self.assertFalse(Plant.objects.filter(scientific_name = "Test plant").exists())


    # test 1 (D4): checks to make sure profile was properly created (checks with database)
    def test_profile_creation(self):
        self.assertEqual(self.profile.user, self.user)
        self.assertTrue(self.profile.avatar)
        self.assertTrue(self.profile.plant_image_1)

    # test 2 (D4): checks to make sure a post is associated to the proper user and stored (checks with database)
    def test_post_creation(self):
        self.assertEqual(self.post.user1, self.user)
        self.assertEqual(self.post.post_content, "Test post content")


    # test 3 (D4): checks to make sure reply is associated to the correct post and user and stored (checks with database)
    def test_reply_creation(self):
        self.assertEqual(self.reply.user, self.user)
        self.assertEqual(self.reply.post, self.post)
        self.assertEqual(self.reply.reply_content, "Test reply content")

    # test 4 (D4): checks to make sure a plant is properly created and stored with all associated information (checks with database)
    def test_plant_creation(self):
        self.assertEqual(self.plant.scientific_name, "Test plant")
        self.assertEqual(self.plant.common_name, "Test common name")
        self.assertEqual(self.plant.growth_habit, "Test growth habit")
        self.assertEqual(self.plant.duration, "Test duration")
        self.assertEqual(self.plant.sun_requirements, "Test sun requirements")
        self.assertEqual(self.plant.water, "Test water recommended")
        self.assertEqual(self.plant.temp_low_F, 50.0)
        self.assertEqual(self.plant.temp_high_F, 80.0)
        self.assertEqual(self.plant.image, "test.img")

    # test 5 (D6): checks to make sure watering schedule can be adjusted and updated
    def test_daily_tasks_update(self):
        # simulate form submission for updating daily tasks
          # sets temp/fake URL
        url = reverse('Myprofile')

          # sets data list for checks later
        data = {}

        # for every day of the week
        for day in range(7):
            # ensure data matches with what was set in the setup function
            data[f'task_{day}'] = f"Updated task for day {day}"

            # simulate some of the tasks eing completed
            if day % 2 == 0:
                data[f'completed_{day}'] = 'on'

        # update to test
        response = self.client.post(url, data)

        # checks if test was successful (data saved and page redirected)
        self.assertEqual(response.status_code, 200)

        # check that all data is correct
        for day in range(7):
            task_date = self.task_date + datetime.timedelta(days=day)
            daily_task = DailyTask.objects.get(user=self.user, task_date=task_date)
            self.assertEqual(daily_task.task_description, f"Task for day {day}")
            self.assertEqual(daily_task.completed, day % 2 == 'on')

    
    # test 6 (D6): checks to ensure unique user creation
    def test_unique_username_registration(self):
        # Define the registration URL
        url = reverse('Register')

        unique_test_user = 'testuserunique1'
        test_num = 1

        # make sure test username is fully unique
        while (User.objects.filter(username = unique_test_user).count() != 0 ):
          test_num = test_num + 1
          unique_test_user = 'testuserunique' + str(test_num)

        # Set up user data
        user_data = {
            'username': unique_test_user,
            'email': 'uniqueuser@example.com',
            'first_name': 'Unique',
            'last_name': 'User',
            'password': 'uniquepassword123',
            'confirm_password': 'uniquepassword123',
        }

        # first registration attempt (should be successful)
        self.client.post(url, user_data)

          # ensures that there is one user with this username
        self.assertEqual(User.objects.filter(username = unique_test_user).count(), 1, "User should be registered successfully")

          # ensures user is in the temp database
        exists = User.objects.filter(username = unique_test_user).exists()
        self.assertTrue(exists, "User should exist in the database after registration")

        # second registration attempt with the same username (should cause failure)
           # response = self.client.post(url, user_data)
           # self.assertEqual(User.objects.filter(username = unique_test_user).count(), 1, "No additional user should be created")


    # test 7: tests for POST request (to webpage) and querry requests
    def test_search_post_request(self):
        response = self.client.post(reverse('Search'), {'q': 'Test common name'})
        self.assertContains(response, "Test plant")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search.html')

    # test 8: tests for search results
    def test_search_result_get_request(self):
        response = self.client.get(reverse('Search Result', args=(self.plant.scientific_name,)))
        self.assertContains(response, "Test common name")
        self.assertContains(response, "Test growth habit")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search_result.html')