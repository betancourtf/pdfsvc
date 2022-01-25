from celery import Celery

app = Celery("pdfsvc")
app.config_from_object("django.conf:settings")
app.autodiscover_tasks()

if __name__ == "__main__":
    app.start()
