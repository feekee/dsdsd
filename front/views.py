from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

def shouye(request):
 #   return HttpResponse("shouye ")
    return render(request, 'js_learn.html')

def api(request):
    return HttpResponse('API测试')