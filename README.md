# Deploying a modern Python application

This repo contains the code for the Medium posts. It begins by creating a simple Django PDF creating app, and builds on more complicated topics.


## Purpose

The posts were born from the lack of similar project while trying to learn. Many posts are being written to use more complicated stacks, that usually include Kubernetes. The idea of this is to build a production ready stack/workflow using simpler solutions.

Read the posts for more information.

## The App

The folder `pdfsvc` is a basic Django app to generate PDF from HTML pages. The idea is to tackle a problem that's not as simple as a Tasks app and that will require more analysis to solve, while being simple enough to understand even for relative new comers to Python/Django.

### Running the improved web app and the workers
To run the improved app that now uses a queue, use:
```
docker compose up -d
```
The RabbitMQ manager will be available at [http://localhost:15672](http://localhost:15672).

If you want to load test the new code use the last's episode commands.

The full blog post is available here: [Episode 5 - Handling expensive  tasks with Celery and RabbitMQ](https://medium.com/@betancourt.francisco/episode-5-handling-expensive-tasks-with-celery-and-rabbitmq-118fadeaf475)

### Running the load testing (Episode 4)
To run both the app and the load test two compose files must be passed when starting up:
```
docker compose -f docker-compose.yml -f docker-compose.locust.yml up -d
docker exec -it pdfsvc-web-1 bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
The Locust web interface will be available at [http://localhost:8089](http://localhost:8089), while the Django REST Framework API will be available at [http://localhost:8000/api/](http://localhost:8000/api/)

The full blog post is available here : [Episode 4 — Testing your Python/Django app’s performance](https://medium.com/@betancourt.francisco/episode-4-testing-your-python-django-apps-performance-4661f5e78f85)

### Running with containers (Episode 3)
The project includes a `Dockerfile` and a `docker-compose.yml`file to run it inside a container. Simply run the commands:
```
docker compose build
docker compose up
docker exec -it pdfsvc-web-1 bash
python manage.py migrate
python manage.py createsuperuser
```
After running the commands above the project will be running and you will have a user to login to the Django Admin and test the pdf functionality still works.

The full blog post is available here: [Episode 3 — Containerizing a Python/Django App](https://medium.com/@betancourt.francisco/episode-3-containerizing-a-python-django-app-5cd952bea204)


### Running locally (Episode 2)

The proyect will evolve with every post. We start by running the app on the local machine, using a virtual environment. A requirements file is provided in the Django app folder. After clonning the project you must make migrations and apply them, we begin using `sqlite` so no database is needed. The commands to run are:

```
python manage.py makemigrations
python manage.py migrate
```

After running the migrations you can start the app locally running the development server with:

```
python manage.py runserver
```

We begin by interacting with the basic model and functionality using the Django Admin, so you need to create a staf user with the command:

```
python manage.py createsuperuser
```

Once in the Django Admin, to test the PDF generation functionality simply add a new "Page Request". You can use any valid URL. PDF rendering is then handled with Django signals.

The full blog post is available here: [Episode 2 — Creating a PDF generating Django Application](https://medium.com/@betancourt.francisco/episode-2-creating-a-pdf-generating-django-application-73a31f332fd4)
