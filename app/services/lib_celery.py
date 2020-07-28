from celery import Celery


def make_celery(app):
    celery = Celery(
        'tasks',
        backend='amqp://tw-site-grabber-6924.hostman.site:80',
        broker='amqp://tw-site-grabber-6924.hostman.site:80',
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery
