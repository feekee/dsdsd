from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

def shouye(request):
 #   return HttpResponse("shouye ")
    return render(request, 'daohang.html')
