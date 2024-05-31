from django.shortcuts import render,HttpResponse

def second(request):
  info = [1, 2, 3, 4, 5]
  return  render(request,'second/second.html', {'info':info})
