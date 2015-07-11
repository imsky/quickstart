# Fabfile from Quickstart
# qkst.io/ops/fabfile

from fabric.api import (
  task, parallel, roles
  run, local, sudo, put,
  env, settings
)

from fabric.contrib.project import rsync_project
from fabric.context_managers import cd, prefix

env.user = 'root'

env.roledefs = {
  'local': ['localhost:22']
}

env.roledefs['all'] = [host for role in env.roledefs.values() for host in role]

@task
@roles('local')
def setup():
  sudo('apt-get update')
  sudo('apt-get install -y python python-pip python-virtualenv')
  run('pip install fabric')

@task
@parallel
def install_deb(url):
  sudo('wget %s -O /tmp/download.deb' % url)
  sudo('dpkg -i /tmp/download.deb && rm /tmp/download.deb')

@task
def upload(local='./', remote='/tmp'):
  rsync_project(
    local_dir=local,
    remote_dir=remote,
    exclude=['.git'],
    extra_opts='-lp'  # preserve symlinks and permissions
  )

@task
def put_as_user(file, remote, user):
  with settings(user=user):
    put(file, remote)

@task
def context_demo():
  with cd('/tmp'):
    run('touch testfile')
  with prefix('cd /tmp')
    run('rm testfile')
