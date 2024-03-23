### Instructions:
For this deliverable, you should have a fully functional piece of software that delivers a set of features (don’t need to be the complete set, but it needs to be a working prototype). Structure your deliverable according to the following sections. See the Team Project Instructions for details about formatting. 


## 1. Introduction (Karissa)
Provide a short paragraph that describes your system. This paragraph should contain the value proposition and a description of the main features of the software. At the end of the introduction, include a link to your project on GitHub.


Plant Pals helps plant owners grow (and not kill their plants) by providing information on to tend to desired plants.  It also provides a community that gives everyone a green thumb! The software's main features are creating/replying to discussion posts, creating an account, and being able to search for different plants within our database system. 
https://github.com/ao994/plant-pals

Grading criteria (1 point): This section will be evaluated in terms of correctness, completeness, thoroughness, consistency, coherence, and adequate use of language. The description should be consistent with the current state of the project. You should include the link to GitHub.

## 2. Implemented requirements:
List in this section, the requirements and associated pull request that you implemented for this release, following the example below---include the description of the requirement, a link to the issue, a link to the pull request(s) that implement the requirement, who implemented the requirement, who approved it, and a print screen that depicts the implemented feature (if applicable). I expect that you implement the features you specified in your MVP (c.f. D.2 Requirements). 
Order the requirements below by the name of the student who implemented them. All the members of the group should have worked on implementation activities and submitted pull requests. Only stable code should be included in the release. The code that is still under development should be in branches. See the example:
Requirement: As a new account holder, I want to easily make my profile so that I can document my plants.
Issue: https://github.com/ao994/plant-pals/issues/31 
Pull request: 
https://github.com/ao994/plant-pals/pull/2 (initial upload)
https://github.com/ao994/plant-pals/pull/70 (formatted upload)
Implemented by: Haley Berger / Andrew Ortega
Approved by: Alyssa Ortiz (but uploaded by Haley Berger to get all base files uploaded)
Print screen:




#### Requirement: 
> "As a community member, I want to post to a discussion so that I can ask questions to more experienced gardeners"
- Issue: https://github.com/ao994/plant-pals/issues/30
- Pull request: https://github.com/ao994/plant-pals/pull/62
	- Implemented by: Haley Berger / Karissa Smallwood
	- Approved by: Alyssa Ortiz

Print screen:
 





#### Requirement: 
> "As an experienced gardener, I want to find and respond to discussions so that I can help people get into plant ownership."
- Issue: https://github.com/ao994/plant-pals/issues/34#issue-2131157582
- Pull requests: https://github.com/ao994/plant-pals/pull/2 (initial creation), 
https://github.com/ao994/plant-pals/pull/84 (edit viewing)
	- Implemented by: Haley Berger / Karissa Smallwood
	- Approved by: Alex King & Karissa Smallwood

Print screen:




#### Requirement: 
> "As a user, I want to have a decorated user profile to make my profile match the website."
- Issue:  https://github.com/ao994/plant-pals/issues/41
- Pull request: https://github.com/ao994/plant-pals/pull/58
	- Implemented by: Haley Kloss
	- Approved by: Haley Berger

Print screen: 




#### Requirement: 
> "As a database manager, I want to be able to add/remove/edit plants so that information stays up-to-date and is easily manageable."
- Issue: https://github.com/ao994/plant-pals/issues/38
- Pull request: https://github.com/ao994/plant-pals/pull/82
	- Implemented by: Alyssa Ortiz
	- Approved by: Karissa Smallwood

Print screen:




#### Requirement: 
> "As an admin, I want to easily moderate so the website stays informative and good-natured."
- Issue: https://github.com/ao994/plant-pals/issues/35
- Pull requests: https://github.com/ao994/plant-pals/pull/2 (moderation for discussion board), 
https://github.com/ao994/plant-pals/pull/82 (moderation for plants)
	- Implemented by: Haley Berger / Alyssa Ortiz
	- Approved by: Alex King

Print screen: 





#### Requirement: 
> "As an older person without much technological savvy, I want to be able to navigate around the website easily so that I can do what I need to without getting confused."
- Issue: https://github.com/ao994/plant-pals/issues/32 
- Pull requests: https://github.com/ao994/plant-pals/pull/2 (initial upload), 
https://github.com/ao994/plant-pals/pull/62 (formatting edit)
	- Implemented by: Haley Berger
	- Approved by: Andrew Ortega

Print screen:






#### Requirement: Configure Docker on server
- Issue: https://github.com/ao994/plant-pals/issues/4 
- Pull request: https://github.com/ao994/plant-pals/pull/85 
	- Implemented by: Alex Kingt
	- Approved by: Haley Berger
   
Print screen: 









All source code should be submitted by means of pull requests and the scrum master in the team should review and approve each pull request. For more information about pull requests: https://help.github.com/articles/about-pull-requests/
  
Grading criteria (10 points): This section will be evaluated in terms of correctness, completeness, thoroughness, consistency, coherence, adequate use of language, and amount of work put into the implementation. Students can receive different grades depending on their involvement. It is expected that all members contribute with non-trivial implementation. All pull requests should be approved and integrated by the scrum master. You should follow an adequate workflow (description of the requirement on the issue tracker, submission of the implemented requirement as a pull request, and review of the pull request by another developer). 

## 3. Tests (Haley B)
You should implement automated tests that aim to verify the correct behavior of your code. Provide the following information:
Test framework you used to develop your tests (e.g., JUnit, unittest, pytest, etc.)
Link to your GitHub folder where your automated unit tests are located
An example of a test case. Include in your answer a GitHub link to the class being tested and to the test
A print screen showing the result of the execution of the automated tests


Test framework: Unittest - specifically a subclass of unitest developed by/for Django.


Example test case:
The following is an example of one of our test cases. This test case specifically attempts to add a plant to the database and then checks if the information in the database is as expected.


GitHub automated test file: https://github.com/ao994/plant-pals/blob/main/Code/plant-pals/profile_of_user/tests.py 
	Class file link: https://github.com/ao994/plant-pals/blob/main/Code/plant-pals/profile_of_user/models.py 


It should be quickly noted that the test files automatically run as follows:
Calls the setup function
Calls the first individual test function in line
Calls the cleanup function
The process resets with the individual test being the next one in line. It will continue to run until all test cases have been run through.
The reason we currently have the setup/teardown function running everything is that most of the information connects. Let’s look at the profile class. A post connects with a specific profile. It can be similarly observed for a reply. A reply connects to a specific user, but it also connects to an initial post. As a result, other data needs to be defined to run some of the tests. For that reason, we have the file laid out with one setup and cleanup function, that also have individual functions for each test. Below is an example of one test case process.
Setup (creates a new object (a new/test plant) using our Plant model; this also adds it to a temporary database created by Django):

Data validation/assertion (confirms that the information in the database matches the information assigned):

Cleanup (removes the added database information to prepare for next test/ confirm that information is properly removed when deleted)



Plant model aside, we have a test case for every model we have made (posts, replies, and profile). 


Below are the test results:

Each ‘.’ represents a successful run of a single test case. There are four ‘.’ because we have four test cases. If one presented an error, the ‘.’ would be replaced with an ‘E’. If one presented a failure, the ‘.’ would be replaced with an ‘F’. The results presented show successful test runs.




Grading criteria (4 points): You should have an adequate number of automated tests. They should be well-written to exercise the main components of your system, covering the relevant inputs.

## 4. Adopted technologies (Haley Berger & Alex)
List the adopted technologies with a brief description and justification for choosing them.
Django (Haley B) - Django is a Python-based, high-level web framework. It has its own URL routing, database models, templates, file structure, and testing system. These ease-of-use features allow us to focus more on the logistics side of how things should run rather than how to get them running. Django comes with a built-in admin panel as well, allowing us to easily access necessary (otherwise encrypted) database information. Some of this information isn’t viewable, such as passwords or other sensitive data. On that note, Django also offers a lot of security features that help protect against things like SQL injections. Django, being free and Python-based, also has a large fanbase of users who made tutorials on various functionalities provided by Django as well as how to build simple websites with it. This drew us in because we know that if we run across an issue, we will most likely be able to find the solution somewhere on the internet. In addition to that, using web frameworks is something that nobody in the group had experience with. We thought it would be a good idea to learn.
Docker (Alex) - Docker is a containerization software to deliver OS-level virtualization similar to that of a virtual machine. The advantage is that docker requires fewer resources by using the host machine’s operating systems services instead of virtualizing an entire guest operating system for each virtual machine. This not only delivers enhanced performance, but also portability, where a docker container is essentially guaranteed to run across all hardware identically if configured properly. This eliminates the issue of software working improperly on deployment but functioning on developer machines, or vice versa. In our case, we only use docker for deployment, as the learning curve would slow down development. Instead, we use Python’s built-in virtual environment module to guarantee all our machines have an identical Python environment and dependencies, which is enough for the scope of our project with our small team. Our pipeline involves pulling the code from the launch-test branch in our GitHub repository, building it using a custom docker-compose.yml file, and pushing this image to a GitHub Container Registry assigned to my account. Then, I SSH into the server, use docker pull to save the latest image to the machine, stop the current container, and start a new container based on the newest image. We use a special docker run command that exposes port 80 and creates a volume mapping. Exposing port 80 allows anyone with access to the internet to access the site over an HTTP connection. The volume mapping is created to allow the container to access the database stored on the server, allowing the data to persist. This means the database containing all user information, posts, and plant information is not wiped every time we deploy a new image due to making changes in the code. Once the docker run command is run, the website is deployed and accessible to the public.
DigitalOcean (Alex) - DigitalOcean is the hosting provider we have selected for our project due to their reputation of being user-friendly and having good customer support. We use a Droplet, DigitalOcean’s name for a Virtual Private Server (VPS). Our Droplet is running Ubuntu 22.04, on which we have installed the Docker engine, which runs the container containing our code. We access this server via SSH, authenticated via an Ed25519 SSH key. Via SSH, we can update the software, manage dependencies, and run the container which runs our code.
GitHub (Alex) - GitHub is a multi-use developer platform with a deep set of features. Our project utilizes the repository syncing capability, to synchronize our code and handle merging into the main branch, to host our containers in GitHub Container Registry, and GitHub’s issue tracker to assign tasks and keep progress going consistently. 
Pillow (Haley B) - Pillow is the only extra Python library we added. It is a version of a different library called PIL (Python Imaging Library). We use this extra library to add image-processing capabilities to our Python code. It supports a large range of file types as well, including JPEG, PNG, GIF, BMP, and TIFF. We want to have things like profile pictures and plant images, so a library for image processing was necessary. After some research, this was the one we settled on due to the ease of use and large number of supporting file types.
Python VENV (Haley B) - Due to some issues with getting Docker to work on everyone's computer, we instead decided to get everyone set up with a Python virtual environment. In this environment, we had everyone pip install the same things: Django and Pillow. Through this environment, we can test our website in a secluded space that is consistent across the team.
Grading criteria (1 point): This section will be evaluated in terms of correctness, completeness, thoroughness, consistency, coherence, and adequate use of language.

## 5. Learning/training (Alyssa)
Describe the strategies employed by the team to learn the adopted technologies. 
Grading criteria (1 point): This section will be evaluated in terms of correctness, completeness, thoroughness, consistency, coherence, and adequate use of language.








## 6. Deployment (Alex)
Provide a link for the system in production and describe how you are deploying your system: 64.23.151.143/
Deployment pipeline:
Pull code from GitHub -> build Docker image using Docker compose -> push Docker image to GitHub Container Registry -> SSH into DigitalOcean Droplet (Virtual Private Server) -> pull latest Docker image -> kill running container -> run latest Docker image


 Grading criteria (3 points): This section will be graded based on the adequate use of the technology and its adequate description.
## 7. Licensing (Andy)
Inform the license you adopted for your source code (remember to configure GitHub accordingly). Explain why you adopted this license. For more information, check https://choosealicense.com/
The license chosen was the MIT license. This license was chosen because it was free and it matched the needs that were required for our project/website.  
https://github.com/ao994/plant-pals/blob/new-main/LICENSE
Grading criteria (1 point): This section will be evaluated in terms of correctness, completeness, thoroughness, consistency, coherence, and adequate use of language.

## 8. README File (Haley K)
You should also prepare your repository for receiving new contributors. You should prepare a README.md file. See an example at https://gist.github.com/PurpleBooth/109311bb0361f32d87a2
. In the README file, the current version should be stated. You should follow the Semantic Versioning


 schema. Tag the GitHub repository accordingly (see Git Basics Tagging
Links to an external site.). 
Your repository should contain a CONTRIBUTING.md file, a LICENSE file, and a CODE_OF_CONDUCT.md file. Search online for some examples of these files. In this section of the deliverable, put links to these files on GitHub.
Link to README File: https://github.com/ao994/plant-pals/blob/main/README.md
Grading criteria (3 points): This section will be based on the presence and quality of the information presented in the files.

## 9. Look & feel (Haley K)
Describe the approach you adopted to design your user interface. Include some screenshots.
In making a user interface, we wanted the website to be very easy to navigate, with a few main pages listed clearly on the top for people to click through. 



We also wanted Plant Pals to be easy to use on different devices, so it is very adaptive to different screen sizes.



We tried to make the colors of the website earthy, with lots of browns and greens used to invoke plant life. We also incorporated images of plants and flowers in the backgrounds of some pages, to further this style.



We used many boxes with rounded edges to keep information separate and digestible while avoiding harsh corners. This allowed for a better look and an easier viewing experience for the users.

Grading criteria (3 points): This section will be graded based on the appearance (aesthetics) and usability (ease of use) of the system.

## 10. Lessons learned (Haley K)
In retrospective, describe what your team learned during this first release and what you are planning to change for the second release. 
In retrospect, we learned a lot between our first and second releases. Although we got a bulk of the work done in the first release, we really worked on refinement in the second. Rather than rushing to just put something together, we went back and made what we had much more aesthetically pleasing, easier to use, more flexible, and overall higher quality.
 We also made sure that we understood all the steps we were taking, rather than just cobbling together commands until things started to work. In the first release, we were much less confident in making sure that everything was running smoothly, as we were not quite sure what was actually working beneath the hood and how. By the second release, we learned a lot about what we had done while going through the refinement process, allowing us to work more efficiently and produce better code and results.
The team also learned how to work together better by the second release. The first couple weeks of the project gave us the chance to learn about each other's strengths and working styles, so that after the first release we had enough information to really distribute work effectively and work together well. Overall, the processes leading up to the second release were much more confident and seamless than in the first release.


Grading criteria (2 points): Adequate reflection about problems and solutions, clear description with adequate use of language. 
## 11. Demo (Alex)
Include a link to a video showing the system working.
Grading criteria (6 points): This section will be graded based on the quality of the video and on the evidence that the features are running as expected. Additional criteria are the relevance of the demonstrated functionalities, the correctness of the functionalities, and the quality of the developed system from the external point of view (user interface).


