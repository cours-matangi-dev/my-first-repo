# -*- coding:Utf8 -*-

bind = "0.0.0.0:5000"
workers = 1
wsgi_app = 'app:app'
worker_class='gevent'
accesslog = '-'
errorlog = '-'
proc_name = 'app'
keepalive = 4
threads = 2
timeout = 600
pidfile = 'app.pid'
user = 'user'
group = 'user'
