GROWSHARE
---

<img src="/static/img/login.jpg" width="500">

GrowShare is a Flask web app dedicated to helping user's find local produce in their area. Employing the Google Maps JavaScript API for geolocation purposes, GrowShare permits users to search for food type, key words and distance, using SQLAlchemy to query the Postgres database and returning search results. 

### Table of Contents 

1. [Technologies](#technologies)
2. [Features](#features)
3. [Installation](#installation)
4. [Deployment](#deployment) 
5. [Author](#author) 

## <a name="technologies"></a>Technologies

**Front-end:** [HTML5](http://www.w3schools.com/html/), [CSS](http://www.w3schools.com/css/), [Bootstrap](http://getbootstrap.com), [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript), [jQuery](https://jquery.com/)

**Back-end:** [Python](https://www.python.org/), [Flask](http://flask.pocoo.org/), [Jinja2](http://jinja.pocoo.org/docs/dev/), [PostgreSQL](http://www.postgresql.org/), [SQLAlchemy](http://www.sqlalchemy.org/)

**API:** [Google Maps](https://developers.google.com/maps/documentation/javascript/)

## <a name="features"></a>Features
###Landing page:
<img align="center" src="/static/img/register.jpg" width="500">

+ Users can register for an account. 
+ Users can log in if they already have an existing account. 
+ The user's information is saved to the session once the user is logged in. Using SQLAlchemy to query the Postgres database, the user object is returned which is then used to access user information.

###Dashboard
<img align="center" src="/static/img/dashboard.jpg" width="500">

+ Users can query for food type, key words and distance
+ Google Maps allows for distance viewing
+ Results are presented after being identified in the Postgres database

## <a name="installation"></a>Installation
As GrowShare has not yet been deployed, please follow these instructions to run GrowShare locally on your machine:

### Prerequisite: 

Install [PostgreSQL](http://postgresapp.com) (Mac OSX).

Postgres needs to be running in order for the app to work. It is running when you see the elephant icon:

Add /bin directory to your path to use PostgreSQL commands and install the Python library.

Use Sublime to edit `~/.bash_profile` or `~/.profile`, and add:

```export PATH=/Applications/Postgres.app/Contents/Versions/9.5/bin/:$PATH``` 

### Set up GrowShare

Clone this repository:

```$ git clone https://github.com/Afraysse/grow_share.git```

Create a virtual environment and activate it:

```
$ virtualenv env
$ source env/bin/activate
```
Install the dependencies:

```$ pip install -r requirements.txt```

Run PostgreSQL (make sure elephant icon is active).

Create database with the name `growshare`.

```$ createdb ratings```

Seed the database with movies, users, and ratings:

```$ python seed.py```

Finally, to run the app, start the server:

```$ python server.py```

Go to `localhost:5000` in your browser to start using GrowShare!

## <a name="deployment"></a>Deployment
Deployment details coming very soon!

## <a name="author"></a>Author  
Annie Fraysse is a Software Engineer living in the San Francisco Bay Area. <br>
[LinkedIn](https://www.linkedin.com/in/annefraysse) | [Email](mailto:fraysse.anne@gmail.com) 
