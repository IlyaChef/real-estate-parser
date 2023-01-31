from celery import Celery

from __init__ import create_app
from . import get_avito_ads

flask_app = create_app()
celery_app = Celery('tasks', broker='redis://localhost:6379/0')

@celery_app.task
def avito_scrape():
    with flask_app.app_context():
        get_avito_ads.scrape()


