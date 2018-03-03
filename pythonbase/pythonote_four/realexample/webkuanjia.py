#!/usr/bin/env python
#coding:utf-8




from  wsgiref.simple_server import make_server

class Handler(object):




      def index(self):
          return  'index'

      def  news(self):
          return  'news'




      def RunServer(environ,start_response):
          start_response('200 ok',[('Content-type','text/html')])
          url=environ['PATH_INFO']
          temp=url.split('/')[1]
          obj=Handler()
          is_exist=hasattr(obj,temp)
          if is_exist:
             func=getattr(obj,temp)
             ret=func()
             return ret
          else:
              return '404  not found'



      if __name__=='__main__':
           httpd=make_server('',8001,RunServer)
           print "Serving HTTP on port 8000..."
           httpd.serve_forever()










