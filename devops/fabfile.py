# Fabfile from Quickstart
# qkst.io/devops/fabfile

from fabric.api import (
    task, parallel, roles,
    run, local, sudo, put,
    env, settings
)

from fabric.contrib.project import rsync_project
from fabric.context_managers import cd, prefix
from fabric.tasks import execute

env.hosts = ['root@localhost:22']


@task
def bootstrap():
    sudo('apt-get update')
    sudo('apt-get install -y sysstat wget unzip htop dtach')


@task
def start():
    execute('service', 'cron')


@task
def service(name, action='start'):
    sudo('service {0} {1} || true'.format(name, action))


@task
def background(process, name='bgprocess'):
    run('dtach -n `mktemp -u /tmp/{0}.XXXXX` {1}'.format(process, name))


@task
def install_deb(url):
    sudo('wget {0} -O /tmp/download.deb'.format(url))
    sudo('dpkg -i /tmp/download.deb && rm /tmp/download.deb')


@task
def status():
    run('service --status-all')
    run('vmstat')
    run('df -h')
    run('iostat')


@task
def upload(local='./', remote='/tmp'):
    rsync_project(
        local_dir=local,
        remote_dir=remote,
        exclude=['.git', '*.pyc', '.DS_Store'],
        extra_opts='-lp'  # preserve symlinks and permissions
    )


@task
def put_as_user(file, remote, user):
    with settings(user=user):
        put(file, remote)
