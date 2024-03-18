# Plant Pals


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 
Run the following commands in the command line: 

Windows:
py -m venv .venv
.venv\Scripts\activate
pip install django
pip install pillow
python manage.py makemigrations
python manage.py migrate
git clone https://github.com/ao994/plant-pals.git
cd plant-pals
cd plant-pals
python manage.py runserver


### Prerequisites
Install: 

python: go to https://www.python.org/downloads/  download the most recent release for your computer  run the installer
django: run command pip install django
pillow: run command pip install pillow

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

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

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
