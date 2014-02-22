from fabric.api import local


def devel():
    local('jekyll server --auto ')


def build():
    local('jekyll build')


def deploy():
    build()
    local('rsync -rtv _site/ site@rosedu.org:lists.rosedu.org/ --exclude env')
