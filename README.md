# Deploying a modern Python application

This repo contains the code for the Medium posts. It begins by creating a simple Django PDF creating app, and builds on more complicated topics.


## Purpose

The posts were born from the lack of similar project while trying to learn. Many posts are being written to use more complicated stacks, that usually include Kubernetes. The idea of this is to build a production ready stack/workflow using simpler solutions.

Read the posts for more information.

## The App

The folder `pdfsvc` is a basic Django app to generate PDF from HTML pages. The idea is to tackle a problem that's not as simple as a Tasks app and that will require more analysis to solve, while being simple enough to understand even for relative new comers to Python/Django.

### Running

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
