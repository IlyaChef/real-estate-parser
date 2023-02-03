from celery import Celery

celery_app = Celery('tasks', broker='redis://localhost:6379/0')


@celery_app.task
def scrap_script():
    with open('/app/get_avito_ads.py', 'rb') as handler:
        exec(handler.read())
