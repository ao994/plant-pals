# Plant Pals

For plant owners who want to connect with a community and get help with plant care, Plant Pals is a website that connects the plant community and offers reliable insights into plant care! Lack of community and information in houseplant ownership affects plant owners; the impact of which is isolation and ineffective plant care that results in plants dying and preventable deaths. Plant Pals helps plant owners grow (and not kill their plants) by providing information and a community that gives everyone a green thumb!

Interested? Visit our website at: [http://64.23.151.143/](http://64.23.151.143/) !

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 
Run the following commands in the command line after download: 

Windows:
   - py -m venv .venv
   
   - .venv\Scripts\activate
   
   - pip install django
   
   - pip install pillow
   
   - python manage.py makemigrations
   
   - python manage.py migrate
   
   - git clone https://github.com/ao994/plant-pals.git
   
   - cd plant-pals
   
   - python manage.py runserver



### Prerequisites
Install: 

- python: go to https://www.python.org/downloads/  download the most recent release for your computer  run the installer
- django: run command pip install django
- pillow: run command pip install pillow

### Installing

A step by step series of examples that tell you how to get a development env running:

1. Create venv vitrual environment: py -m venv .venv
2. Open venv environment:           .venv\Scripts\activate
3. Install django in environment:   pip install django
4. Install django in environment:   pip install pillow
5. Make migrations:                 python manage.py makemigrations
6. Make migrations:                 python manage.py migrate
7. Create clone of project:         git clone https://github.com/ao994/plant-pals.git
8. Enter project:                   cd plant-pals


End with an example of getting some data out of the system or using it for a little demo

### Testing
#### Running the tests
1. In the command line, enter the virtual environment and navigate to where the manage.py file is located.
2. Run the command: python manage.py test
3. The tests will run and results will be displayed.

   Additional notes: a '.' will be displayed for a successful test. An 'E' will be displayed if an error is presented, and a 'F' will be displayed when a failure is presented.
   If four '.' are presented, then each of the four following tests was successful.

#### The Tests
**Test 1:** checks to make sure a profile was properly created (checks with database)

This test creates a test user profile. Data is saved into the profile (fake name, email, et cetera) and then is added to a temporary database. The test confirms that the information in the database is as expected. The test then clears the temporary database, confirming that the information was removed as expected.

**Test 2:** checks to make sure a post is associated with the proper user and stored (checks with database)

This test creates a test post. Data is saved into the post (text) and then is added to a temporary database. The test confirms that the information in the database is as expected and that the post associates with the current user. The test then clears the temporary database, confirming that the information was removed as expected.

**Test 3:** checks to make sure the reply is associated with the correct post and user and stored (checks with database)

This test creates a test reply. Data is saved into the reply (text) and then is added to a temporary database. The test confirms that the information in the database is as expected and that the post associates with the current user and original reply. The test then clears the temporary database, confirming that the information was removed as expected.

**Test 4:** checks to make sure a plant is properly created and stored with all associated information (checks with database)

This test creates a test plant. Data is saved into the made temporary plant (fake name and other plant information) and then is added to a temporary database. The test confirms that the information in the database is as expected. The test then clears the temporary database, confirming that the information was removed as expected.

**It should be noted that tests 1, 2, and 3 (although independent) run with some association with the other. Test three, for example, needs to have a user (profile) from which the reply is posted. A reply also cannot be sent without an original post.**


### Coding Style Tests/ Coding Standards

1. All variables must be self-documenting. Reason: If someone wants to go through and change something, we need to be able to easily identify what to change.
2. Formatting must be consistent. Reason: We want to be able to easily find what we are looking for. If code is inconsistently formatted, that would be difficult.
3. Follow logic. Don't do something in a roundabout way even if it is easier to code. Make it easy to follow. Reason: We want to be able to understand the code when looking at it.
4. No using break unless necessary. Reason: There are very few circumstances where break is needed. It's best to avoid it to keep logic consistent.
5. Avoid global variables. Reason: We really should not need them and it would be hard to track them through code.
6. Keep to useing true or false rather than 1 or 0. Reason: General readability. Makes it easier/faster to understand and track.
7. Use of continue. Reason: There is no reason we should use this and it would just break up code readability.

## Deployment: 
http://64.23.151.143/

This website is deployed in a Docker container running on a Virtual Private Server provided by Digital Ocean (see: Digital Ocean Droplet). The code is all contained within a single image which is used to build a docker container, with a volume mapping to a separate SQLite Database file in the server's filesystem. The Docker container exposes Port 80 so the contents are accessible to the outside world.

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Bootstrap](https://getbootstrap.com/) - CSS assets
* [Pillow]([https://rometools.github.io/rome/](https://pypi.org/project/pillow/)) - Python library

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details contributing. Please also read the code of conduct. 

## Versioning

Version 1.1.0

## Authors

* **Haley Berger** 
* **Haley Kloss**
* **Alex King** 
* **Andrew Ortega**
* **Karissa Smallwood** 
* **Alyssa Ortiz** 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Thank you to Professor Chavez
