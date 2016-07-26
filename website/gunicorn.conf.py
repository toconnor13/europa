from __future__ import unicode_literals
import multiprocessing

bind = "unix:/home/moritz/europa/website/gunicorn.sock"
workers = multiprocessing.cpu_count() * 2 + 1
errorlog = "/home/moritz/logs/website_error.log"
loglevel = "error"
proc_name = "website"
