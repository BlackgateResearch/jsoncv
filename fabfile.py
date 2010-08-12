from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm

#env.hosts = ['localhost']

def test():
    with settings(warn_only=True):
        result = local('./manage.py test', capture=False)
    if result.failed and not confirm("Tests failed. Continue anyway?"):
        abort("Aborting at user request.")

def clean():
    env.warn_only = True
    local('rm *.pyc')
    local('rm *~')
    local('rm cv/*.pyc')
    local('rm cv/*~')

def pack():
    local('tar czf /tmp/my_project.tgz .', capture=False)

def prepare_deploy():
    test()
    pack()

def deploy():
    put('/tmp/my_project.tgz', '/tmp/')
    with cd('/srv/django/my_project/'):
        run('tar xzf /tmp/my_project.tgz')
        run('touch app.wsgi')
