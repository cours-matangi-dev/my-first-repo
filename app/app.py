#!/usr/bin/python3
# coding: utf-8
"""
this is app.py for flask-tutorial (sondage example)
"""
from flask import Flask
#pylint:disable=import-error
from handlers.routes import configure_routes


# create the Flask app
class ReverseProxied(object
                     ):  #for serving the website at /blabla or other path

    def __init__(self, app, script_name=None, scheme=None, server=None):
        self.app = app
        self.script_name = script_name
        self.scheme = scheme
        self.server = server

    def __call__(self, environ, start_response):
        script_name = environ.get('HTTP_X_SCRIPT_NAME', '') or self.script_name
        if script_name:
            environ['SCRIPT_NAME'] = script_name
            path_info = environ['PATH_INFO']
            if path_info.startswith(script_name):
                environ['PATH_INFO'] = path_info[len(script_name):]
        scheme = environ.get('HTTP_X_SCHEME', '') or self.scheme
        if scheme:
            environ['wsgi.url_scheme'] = scheme
        server = environ.get('HTTP_X_FORWARDED_SERVER', '') or self.server
        if server:
            environ['HTTP_HOST'] = server
        return self.app(environ, start_response)


appli = Flask(__name__)
appli.config['SECRET_KEY'] = '36b788e06d0c84d524eb881879ac7e2f66352b6480717bb9'
appli.wsgi_app = ReverseProxied(appli.wsgi_app)
configure_routes(appli)

if __name__ == '__main__':
    # run app in debug mode on port 5000
    #pylint:disable=redefined-outer-name
    appli.run(debug=True, host="0.0.0.0", port=5000)
