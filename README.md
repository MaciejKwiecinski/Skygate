# Skygate API
 


## First installation

When you turn on this repository first time, you have to turn on terminal.
In right directory use command ```chmod 777 ./install.sh```, and then install script
``` ./install.sh ```.

### Local settings

In directory ```skygate``` is located file ```localsettings.py.txt```, you have to edit it, and change file extension 
to ```localsettings.py```. Inside this file, you have to change: 
```
NAME
USER
PASSWORD
HOST
```
### Docker  installation

In settings.py file (lines from 75 to 90), change database for ```DOCKER DB```.
Now you are ready to go and able to run ```docker-compose up --build```,
then you have to use command ``` python3 manage.py makemigrations ```. and then run migrations
``` python3 manage.py migrate ```.
In this case you need to create super user by running ```docker-compose run web python3 manage.py createsuperuser```
than, start server again with ```docker-compose up```.
Now you can check all the functionality .


### Skyphrases

In directory ```Exercise_2_and_3``` is file ```kyphrases```. You can run it by command ```python3 skyphrases.py```, and in console, you will see the answer to the question:

```
How many skyphrases are valid (383)
```

## I wrote in JSON

In directory ```Exercise_2_and_3``` is file ```Json```You can run it by command ```python3 Json```, and in console, you will see the answer to the question:

```
What is the sum of all numbers in the document? (111754)
```

## Built With

* [Django](https://www.djangoproject.com/)
* [Django REST](https://www.django-rest-framework.org/)
* [Python](https://www.python.org/)


