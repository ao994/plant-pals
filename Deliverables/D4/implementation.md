## 1. Introduction (Karissa)
Plant Pals helps plant owners grow (and not kill their plants) by providing information on to tend to desired plants.  It also provides a community that gives everyone a green thumb! The software's main features are creating/replying to discussion posts, creating an account, and being able to search for different plants within our system. 

https://github.com/ao994/plant-pals

## 2. Implemented Requirements:
#### Requirement: 
> As a new account holder, I want to easily make my profile so that I can document my plants.
- Issue: https://github.com/ao994/plant-pals/issues/31 
- Pull request: 
https://github.com/ao994/plant-pals/pull/2 (initial upload)
https://github.com/ao994/plant-pals/pull/70 (formatted upload)
	- Implemented by: Haley Berger / Andrew Ortega
	- Approved by: Alyssa Ortiz (but uploaded by Haley Berger to get all base files uploaded)

Print screen:
![alt text][story1]



#### Requirement: 
> "As a community member, I want to post to a discussion so that I can ask questions to more experienced gardeners"
- Issue: https://github.com/ao994/plant-pals/issues/30
- Pull request: https://github.com/ao994/plant-pals/pull/62
	- Implemented by: Haley Berger / Karissa Smallwood
	- Approved by: Alyssa Ortiz

Print screen:
![alt text][story2]


#### Requirement: 
> "As an experienced gardener, I want to find and respond to discussions so that I can help people get into plant ownership."
- Issue: https://github.com/ao994/plant-pals/issues/34#issue-2131157582
- Pull requests: https://github.com/ao994/plant-pals/pull/2 (initial creation), 
https://github.com/ao994/plant-pals/pull/84 (edit viewing)
	- Implemented by: Haley Berger / Karissa Smallwood
	- Approved by: Alex King & Karissa Smallwood

Print screen:
![alt text][story3]


#### Requirement: 
> "As a user, I want to have a decorated user profile to make my profile match the website."
- Issue:  https://github.com/ao994/plant-pals/issues/41
- Pull request: https://github.com/ao994/plant-pals/pull/58
	- Implemented by: Haley Kloss
	- Approved by: Haley Berger

Print screen: 
![alt text][story4]



#### Requirement: 
> "As a database manager, I want to be able to add/remove/edit plants so that information stays up-to-date and is easily manageable."
- Issue: https://github.com/ao994/plant-pals/issues/38
- Pull request: https://github.com/ao994/plant-pals/pull/82
	- Implemented by: Alyssa Ortiz
	- Approved by: Karissa Smallwood

Print screen:
![alt text][story5]


#### Requirement: 
> "As an admin, I want to easily moderate so the website stays informative and good-natured."
- Issue: https://github.com/ao994/plant-pals/issues/35
- Pull requests: https://github.com/ao994/plant-pals/pull/2 (moderation for discussion board), 
https://github.com/ao994/plant-pals/pull/82 (moderation for plants)
	- Implemented by: Haley Berger / Alyssa Ortiz
	- Approved by: Alex King

Print screen: 
![alt text][story6]


#### Requirement: 
> "As an older person without much technological savvy, I want to be able to navigate around the website easily so that I can do what I need to without getting confused."
- Issue: https://github.com/ao994/plant-pals/issues/32 
- Pull requests: https://github.com/ao994/plant-pals/pull/2 (initial upload), 
https://github.com/ao994/plant-pals/pull/62 (formatting edit)
	- Implemented by: Haley Berger
	- Approved by: Andrew Ortega

Print screen:
![alt text][story7]



#### Requirement: Configure Docker on server
- Issue: https://github.com/ao994/plant-pals/issues/4 
- Pull request: https://github.com/ao994/plant-pals/pull/85 
	- Implemented by: Alex Kingt
	- Approved by: Haley Berger
   
Print screen: 
![alt text][story8]


[story1]: https://github.com/ao994/plant-pals/blob/alex-development/Deliverables/D4/story1.png
[story2]: https://github.com/ao994/plant-pals/blob/alex-development/Deliverables/D4/story2.png
[story3]: https://github.com/ao994/plant-pals/blob/alex-development/Deliverables/D4/story3.png
[story4]: https://github.com/ao994/plant-pals/blob/alex-development/Deliverables/D4/story4.png
[story5]: https://github.com/ao994/plant-pals/blob/alex-development/Deliverables/D4/story5.png
[story6]: https://github.com/ao994/plant-pals/blob/alex-development/Deliverables/D4/story6.png
[story7]: https://github.com/ao994/plant-pals/blob/alex-development/Deliverables/D4/story7.png
[story8]: https://github.com/ao994/plant-pals/blob/alex-development/Deliverables/D4/story8.png



## 3. Tests (Haley Berger)

**Test framework:** Unittest - specifically a subclass of unitest developed by/for Django.


**Example test case:**
The following is an example of one of our test cases. This test case specifically attempts to add a plant to the database and then checks if the information in the database is as expected.


**GitHub automated test file:** https://github.com/ao994/plant-pals/blob/main/Code/plant-pals/profile_of_user/tests.py 
	**Class file link:** https://github.com/ao994/plant-pals/blob/main/Code/plant-pals/profile_of_user/models.py 


It should be quickly noted that the test files automatically run as follows:
1. Calls the setup function
2. Calls the first individual test function in line
3. Calls the cleanup function
4. The process resets with the individual test being the next one in line. It will continue to run until all test cases have been run through.

The reason we currently have the setup/teardown function running everything is that most of the information connects. Let’s look at the profile class. A post connects with a specific profile. It can be similarly observed for a reply. A reply connects to a specific user, but it also connects to an initial post. As a result, other data needs to be defined to run some of the tests. For that reason, we have the file laid out with one setup and cleanup function, that also has individual functions for each test. Below is an example of one test case process.

### Setup (creates a new object (a new/test plant) using our Plant model; this also adds it to a temporary database created by Django):
![alt text][test1]

### Data validation/assertion (confirms that the information in the database matches the information assigned):
![alt text][test2]


### Cleanup (removes the added database information to prepare for next test/ confirm that information is properly removed when deleted)
![alt text][test3]


Plant model aside, we have a test case for every model we have made (posts, replies, and profile). 

Below are the test results:
![alt text][test4]

Each ‘.’ represents a successful run of a single test case. There are four ‘.’ because we have four test cases. If one presented an error, the ‘.’ would be replaced with an ‘E’. If one presented a failure, the ‘.’ would be replaced with an ‘F’. The results presented show successful test runs.


[test1]: https://github.com/ao994/plant-pals/blob/alex-development/Deliverables/D4/test1.png
[test2]: https://github.com/ao994/plant-pals/blob/alex-development/Deliverables/D4/test2.png
[test3]: https://github.com/ao994/plant-pals/blob/alex-development/Deliverables/D4/test3.png
[test4]: https://github.com/ao994/plant-pals/blob/alex-development/Deliverables/D4/test4.png



## 4. Adopted Technologies (Haley Berger & Alex)

+ Django (Haley Berger, Alex) - Django is a Python-based web framework. Our project utilizes Django’s URL routing, SQLite database model, testing system, and user authentication system. These tools allowed us to create a working version of our project within weeks, and the large community of Django users made it easy to troubleshoot. Django being Python-based also enabled our team to pick it up quickly, as we are all more familiar with Python than the Javascript that most other web frameworks are based on.

+ Docker (Alex) - Docker is a containerization software to deliver OS-level virtualization similar to that of a virtual machine. The advantage is that docker requires fewer resources by using the host machine’s operating systems services instead of virtualizing an entire computer’s hard for each virtual machine. By virtualizing the operating system, Docker guarantees that our code will run the same on a developer’s machine as it will on the server once deployed.

+ DigitalOcean (Alex) - DigitalOcean is the hosting provider we have selected for our project due to their reputation of being user-friendly and having good customer support. We use a Droplet, DigitalOcean’s name for a Virtual Private Server (VPS). Our Droplet is running Ubuntu 22.04, on which we have installed the Docker engine, which runs the container containing our code. We access this server via SSH, authenticated via an Ed25519 SSH key. Via SSH, we can update the software, manage dependencies, and run the container which runs our code.

+ GitHub (Alex) - GitHub is a multi-use developer platform with a deep set of features. Our project utilizes the repository syncing capability, to synchronize our code and handle merging into the main branch, to host our containers in GitHub Container Registry, and GitHub’s issue tracker to assign tasks and keep progress going consistently. 

+ Pillow (Haley Berger) - Pillow is the only extra Python library we added. It is a version of a different library called PIL (Python Imaging Library). We use this extra library to add image-processing capabilities to our Python code. It supports a large range of file types as well, including JPEG, PNG, GIF, BMP, and TIFF. We want to have things like profile pictures and plant images, so a library for image processing was necessary. After some research, this was the one we settled on due to the ease of use and large number of supporting file types.

+ Python VENV (Haley Berger) - Due to some issues with getting Docker to work on everyone's computer, we instead decided to get everyone set up with a Python virtual environment. In this environment, we had everyone pip install the same things: Django and Pillow. Through this environment, we can test our website in a secluded space that is consistent across the team.



## 5. Learning/Training (Alyssa)
Our team employed several different technologies in creating our project. Each time we would introduce a new technology, we would find the documentation for it, as well as several other outside resources such as YouTube videos or tutorials explaining how to use it and get started. This would be posted in a dedicated “resources” discord channel, where everyone would be expected to review these resources and ask any questions if they still did not understand. For large changes or technology adoptions, we had meetings to make sure everyone understood and could use this technology correctly. Additional group presentations were provided for more complicated topics and to keep everyone on the same page.



## 6. Deployment (Alex)
**Production System:** http:64.23.151.143

Deployment pipeline:
Pull code from GitHub -> build Docker image using Docker compose -> push Docker image to GitHub Container Registry -> SSH into DigitalOcean Droplet (Virtual Private Server) -> pull latest Docker image -> kill running container -> run latest Docker image

Our pipeline involves pulling the code from the launch-test branch in our GitHub repository, building it using a custom docker-compose.yml file, and pushing this image to a GitHub Container Registry assigned to my (Alex’s) account. Then, I SSH into the server, use docker pull to save the latest image to the machine, stop the current container, and start a new container based on the newest image. I use a special docker run command that exposes port 80 and creates a volume mapping. Exposing port 80 allows anyone with access to the internet to access the site over an HTTP connection. The volume mapping is created to allow the container to access the database stored on the server, allowing the data to persist. This means the database containing all user information, posts, and plant information is not wiped every time we deploy a new image due to making changes in the code. Once the docker run command is run, the website is deployed and accessible to the public.



## 7. Licensing (Andy)
The license chosen was the MIT license. This license was chosen because it was free and it matched the needs that were required for our project/website.  
https://github.com/ao994/plant-pals/blob/new-main/LICENSE



## 8. README File (Haley Kloss)
Link to README File: https://github.com/ao994/plant-pals/blob/main/README.md



## 9. Look & Feel (Haley Kloss)

#### In making a user interface, we wanted the website to be very easy to navigate, with a few main pages listed clearly on the top for people to click through: 
![alt text][look1]


#### We also wanted Plant Pals to be easy to use on different devices, so it is very adaptive to different screen sizes:
![alt text][look2]


#### We tried to make the colors of the website earthy, with lots of browns and greens used to invoke plant life. We also incorporated images of plants and flowers in the backgrounds of some pages, to further this style:
![alt text][look3]


#### We used many boxes with rounded edges to keep information separate and digestible while avoiding harsh corners. This allowed for a better look and an easier viewing experience for the users:
![alt text][look4]


[look1]: https://github.com/ao994/plant-pals/blob/alex-development/Deliverables/D4/look1.png
[look2]: https://github.com/ao994/plant-pals/blob/alex-development/Deliverables/D4/look2.png
[look3]: https://github.com/ao994/plant-pals/blob/alex-development/Deliverables/D4/look3.png
[look4]: https://github.com/ao994/plant-pals/blob/alex-development/Deliverables/D4/look4.png



## 10. Lessons Learned (Haley Kloss)
In retrospect, we learned a lot between our first and second releases. Although we got a bulk of the work done in the first release, we really worked on refinement in the second. Rather than rushing to just put something together, we went back and made what we had much more aesthetically pleasing, easier to use, more flexible, and overall higher quality.

We also made sure that we understood all the steps we were taking, rather than just cobbling together commands until things started to work. In the first release, we were much less confident in making sure that everything was running smoothly, as we were not quite sure what was actually working beneath the hood and how. By the second release, we learned a lot about what we had done while going through the refinement process, allowing us to work more efficiently and produce better code and results.

The team also learned how to work together better by the second release. The first couple weeks of the project gave us the chance to learn about each other's strengths and working styles, so that after the first release we had enough information to really distribute work effectively and work together well. Overall, the processes leading up to the second release were much more confident and seamless than in the first release.



## 11. Demo (Alex)

<a href="http://www.youtube.com/watch?feature=player_embedded&v=UfeOeVB8Sc0
" target="_blank"><img src="http://img.youtube.com/vi/UfeOeVB8Sc0/0.jpg" 
alt="Link to Plant Pals Demo on YouTube" width="480" height="360" border="10" /></a>


