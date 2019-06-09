# Catalog

The aim of this project is to develop an application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.
This project was created in the course of the Full Stack Web Developer Nanodegree Program.

### Tech

Catalog uses follwing open source projects:

* [Flask](http://flask.pocoo.org/) - is a microframework for Python based on Werkzeug, Jinja 2 and good intentions
* [flask-sqlalchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)- is an extension for Flask that adds support for SQLAlchemy to your application.
* [bootstrap](https://getbootstrap.com/)- Bootstrap is an open source toolkit for developing with HTML, CSS, and JS.

### Installation and run
Create and Add your own *client_secrets.json* to the Catalog/Catalog Folder. How to create this file can be found on the following website [developers.google](https://developers.google.com/identity/protocols/OAuth2WebServer)

Install the dependencies from the *requirements.txt* file
```sh
$ pip install -r requirements.txt
```
Run the following python scripts to create and fill the sql database
```sh
$ python CreateDbAndContent.py
```
To run the WebApp 
```sh
$ python run.py
```
 The site is running on http://localhost:5000/
### License
MIT
