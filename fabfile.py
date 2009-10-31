from fabric.api import *

env.user='yG.6059.'
env.hosts=['latentflip.com']
env.root='/home/latentflip/DjangoProjects/RedisWeb'

def deploy():
    git_push()

def git_push():
    local('git push github master')
    run('cd %s; git pull;' % env.root)

def virtualenv():
    run('cd %s; rm -rf env; pip install -E env -r requirements.txt' % env.root)