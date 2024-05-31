from django.shortcuts import render,HttpResponse

def third(request):
    return render(request,'third/third.html')
