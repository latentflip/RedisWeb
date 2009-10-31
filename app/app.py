#!/home/latentflip/DjangoProjects/RedisWeb/env/bin/python

import os, sys, logging
logging.basicConfig(filename='log.txt', level=logging.DEBUG)



logging.debug(sys.path)

activate_this = os.path.expanduser("~/DjangoProjects/RedisWeb/env/bin/activate_this.py")
execfile(activate_this, dict(__file__=activate_this))

import web, redis, inspect

urls = (
  '/', 'index',
  '/([\w\d]+)/([\w\d]+)', 'database',
  '/([\w\d]+)/([\w\d]+)/([\w\d]+)', 'database',
)

db = redis.Redis()
# 
app = web.application(urls, globals())

class database:
    def GET(self, *args):
        try:
            func = getattr(db, args[0])
            nargs = inspect.getargspec(func)[0]
            if len(args)<=len(nargs):
                return func(*args[1:])
            else:
                return "Too many arguments for function: %s" % args[0]
        except:
            return "The function '%s' does not exist." % args[0]

# 
if __name__ == "__main__": app.run()
