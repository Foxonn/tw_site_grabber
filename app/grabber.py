from flask import Flask, request, jsonify, Response
from app.services.lib_services import test_hello_world, parse_site
from app.services.lib_celery import make_celery
from celery.result import AsyncResult
import os

app = Flask(__name__)
celery = make_celery(app)


@app.route('/')
def hello_world():
    return "hello_world"


@app.route('/get_archive/<id_task>')
def get_archive(id_task):
    result = AsyncResult(id_task, app=celery)

    if result.state == 'SUCCESS':
        ziplink = result.get()

        if ziplink and os.path.exists(ziplink):
            *path, zipname = ziplink.split('/')

            path = "/".join(path)

            with open(os.path.join(path, zipname), 'rb') as f:
                data = f.readlines()

            return Response(data, headers={
                'Content-Type': 'application/zip',
                'Content-Disposition': 'attachment; filename=%s;' % zipname
            })


@app.route('/get_status_task/<id_task>')
def get_status_task(id_task):
    result = AsyncResult(id_task, app=celery)

    if result.state == 'SUCCESS':
        ziplink = result.get()
        return jsonify({'link': '/get_archive/' + id_task})

    return jsonify({'state': result.state})


@app.route('/run_parse_site', methods=['POST'])
def run_parse_site():
    site_url = request.form['site_url']
    task = task_parse_site.delay(site_url)
    return jsonify({"id": task.id})


@celery.task(soft_time_limit=60 * 10, time_limit=60 * 15)
def task_parse_site(site_url):
    return parse_site(site_url)
