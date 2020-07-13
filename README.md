# [Kairos Shop Microservice](https://kairosshop.xyz/)

This microservice was maked with the [Flask](https://flask.palletsprojects.com/en/1.1.x/) microframework (v1.1.x). This project is part of the final project of the Platzi Master students (Team Kairos, Cohort 2).

Kairos Shop is a web app that allows you to offer products and compare prices from different supermarkets.

More info: https://www.notion.so/alejozepol/Kairos-d91d3954a8b44d64bd1e70797c9a58b5

## Microservice Scope


This microservice have the duty of:
- Compare the prices of all products in every supermarket.
- Presents the list of products in two diferent ways:
  - buying all product in one supermarket,
  - buying every product in the cheapest place.
- If the total price in more than one supermarket is the same:
  - the microservice will prioritize the nearest supermarket.

## Configurating and runing the code

### Development server

Create a ```config.py``` file, inside the ```app/``` folder, with an instance of the Config class:

```python
class Config:
  SECRET_KEY = ''
```
You can generate the SECRET_KEY in a python console with:

```python
import os
os.urandom(24)
```

Create a virtual environment inside the microservice folder with:

```shell
virtualenv venv
```

Activate the virtual environment:

```shell
source venv/bin/activate  # Linux, Mac

.venv\Scripts\activate  # Windows 10
```

You will need to export two environment variables:

```shell
export FLASK_APP=main.py
export FLASK_ENV=development
```

To run the flask tests, in the console:

```shell
flask test
```

For running the internal server:

```shell
flask run
```

Now, if everything is fine, you should have runnig the server in ```localhost:5000/```

The microservice has several test cases included, to see its work process. You can see the result of these cases using the POST method to send a numeric string:

```
/comparator/?cart=000x
```

where ```x``` is a numerical value between 1 and 8.

### Further help

To learn more help about Flask, check the Flask documentation with ```flask --help ``` or the [Flask Documentation](https://flask.palletsprojects.com/en/1.1.x/).


## Team Kairos (members)

[Additional information of the team.](https://www.notion.so/alejozepol/58ab874c496d4491ab96c4fb6fde2acb?v=aa0c9f4dfed2457680a9bd6cbec57b7f)

* **Armando Rivera** - *Frontend Development* - [GitHub](https://github.com/Armando101), [Twitter](https://twitter.com/ArmandoRN5).

* **Alejandro López Ramírez** - *Design Ux and FrontEnd Development* - [GitHub](https://github.com/alejozepol),  [Website](http://alejozepol.com), [Twitter](https://twitter.com/alejozepol).

* **Néstor Arellano** - *Data Science* - [GitHub](https://github.com/Asoretzu), [Twitter](https://twitter.com/asoretzu).

* **Carlos Enrique Ramírez Flores** - *Backend Development* - [GitHub](https://github.com/linuxcarl), [Website](https://www.carlosramirezflores.com/), [Linkedin](https://www.linkedin.com/in/carlos-enrique-ram%C3%ADrez-flores-5a26475a/).

* **Marco Elizalde** - *Devlop CI CD Backend Development* - [GitHub](https://github.com/marcoETmx),  [Website](http://marcoelizalde.com).

## Expressions of gratitude

* Tell others about this project.
* Invite us a beer.
* Give public thanks.
* Follow us on our social networks and GitHub.
* Etc.
