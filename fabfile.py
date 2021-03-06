from tools.fablib import *

from fabric.api import task

"""
Base configuration
"""
env.project_name = 'ijec'
env.hosts = ['localhost', ]
env.sftp_deploy = True # needed for wpengine
env.domain = 'ijec.dev'

# Environments
@task
def production():
    """
    Work on production environment
    """
    env.settings    = 'production'
    env.hosts       = [ os.environ[ 'IJEC_PRODUCTION_SFTP_HOST' ], ]   # ssh host for production.
    env.user        = os.environ[ 'IJEC_PRODUCTION_SFTP_USER' ]        # ssh user for production.
    env.password    = os.environ[ 'IJEC_PRODUCTION_SFTP_PASSWORD' ]    # ssh password for production.
    env.domain      = 'ijec.wpengine.com'
    env.port        = '2222'

@task
def staging():
    """
    Work on staging environment
    """
    env.settings    = 'staging'
    env.hosts       = [ os.environ[ 'IJEC_STAGING_SFTP_HOST' ], ]   # ssh host for production.
    env.user        = os.environ[ 'IJEC_STAGING_SFTP_USER' ]       # ssh user for production.
    env.password    = os.environ[ 'IJEC_STAGING_SFTP_PASSWORD' ]    # ssh password for production.
    env.domain      = 'ijec.staging.wpengine.com'
    env.port        = '2222'

try:
    from local_fabfile import  *
except ImportError:
    pass
