from pywebcopy import save_website
import zipfile
import os
import shutil
import re


def _init_dir_project(site):
    name_dir = re.findall(r'http(s|):\/\/(.*?)\/', site)[0][1]

    if name_dir.endswith('/'):
        name_dir = name_dir.replace('/', '')

    dir_project = os.path.realpath(os.path.join(
        os.path.dirname(__file__),
        '..',
        '..',
        'copy',
        name_dir))

    os.makedirs(dir_project, exist_ok=True)

    return [dir_project, name_dir]


def _remove_dir(dir_project):
    shutil.rmtree(dir_project)


def _run_copy(project_url, dest_path):

    save_website(
        url=project_url,
        project_folder=dest_path,
        bypass_robots=True,
    )

def run(site):
    dir_project, name_dir = _init_dir_project(site)

    _remove_dir(dir_project)
    _run_copy(site, dir_project)

    return f'{dir_project}/{name_dir}.zip'


if __name__ == '__main__':
    result = run('https://khashtamov.com/ru/')
    print(result)
