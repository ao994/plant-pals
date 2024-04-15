from django.test import TestCase
from .models import Profile, Post, Replie, Plant
from django.contrib.auth.models import User

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


    # cleans up created object after each test in order to start next test fresh
        # is automatically run after each test
    def tearDown(self):
        self.plant.delete()
        self.reply.delete()
        self.post.delete()
        self.profile.delete()

        # checks to make sure data was properly deleted
        self.assertFalse(Profile.objects.filter(user = self.user).exists())
        self.assertFalse(Post.objects.filter(user1 = self.user).exists())
        self.assertFalse(Replie.objects.filter(user = self.user).exists())
        self.assertFalse(Plant.objects.filter(scientific_name = "Test plant").exists())


    # test 1: checks to make sure profile was properly created (checks with database)
    def test_profile_creation(self):
        self.assertEqual(self.profile.user, self.user)
        self.assertTrue(self.profile.avatar)
        self.assertTrue(self.profile.plant_image_1)

    # test 2: checks to make sure a post is associated to the proper user and stored (checks with database)
    def test_post_creation(self):
        self.assertEqual(self.post.user1, self.user)
        self.assertEqual(self.post.post_content, "Test post content")


    # test 3: checks to make sure reply is associated to the correct post and user and stored (checks with database)
    def test_reply_creation(self):
        self.assertEqual(self.reply.user, self.user)
        self.assertEqual(self.reply.post, self.post)
        self.assertEqual(self.reply.reply_content, "Test reply content")

    # test 4: checks to make sure a plant is properly created and stored with all associated information (checks with database)
    def test_plant_creation(self):
        self.assertEqual(self.plant.scientific_name, "Test plant")
        self.assertEqual(self.plant.common_name, "Test common name")
        self.assertEqual(self.plant.growth_habit, "Test growth habit")
        self.assertEqual(self.plant.duration, "Test duration")
        self.assertEqual(self.plant.sun_requirements, "Test sun requirements")
        self.assertEqual(self.plant.water, "Test water recommended")
        self.assertEqual(self.plant.temp_low_F, 50.0)
        self.assertEqual(self.plant.temp_high_F, 80.0)
        self.assertEqual(self.plant.image, "test.html")
