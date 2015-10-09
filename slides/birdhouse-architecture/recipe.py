from birdhousebuilder.recipe import conda, supervisor, nginx

class PyWpsRecipe(object):
    def __init__(self, buildout, name, options):
        # set default options

    def install(self):
        # install pywps with nginx, gunicorn and supervisor
        # generate config files from templates according the options

    def update(self):
        # update configuration
