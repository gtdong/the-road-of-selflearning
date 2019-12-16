from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse

class MyMidd(MiddlewareMixin):
    def process_request(self,request):

        print('我是第一个中间件里面的process_request方法')
        return HttpResponse('akjdasdksjadkl')

    def process_response(self,request,response):
        print('我是第一个中间件里面的process_response方法')
        return response

class MyMidd1(MiddlewareMixin):
    def process_request(self,request):
        print('我是第二个中间件里面的process_request方法')
    def process_response(self,request,response):
        print('我是第二个中间件里面的process_response方法')
        return response