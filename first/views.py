from django.shortcuts import render,HttpResponseRedirect
from first.forms import DjangoForm
from .models import Payment,modelForm
def first(request):
    payment=Payment.objects.all()
    return render(request,'first/index.html', {'payment':payment})
def showForm(request):
    if request.method=='POST':
        form=DjangoForm(request.POST)
        if form.is_valid():
           mobile=form.cleaned_data['mobile']
           laptop=form.cleaned_data['mobile']
           data=modelForm(mobile=mobile,laptop=laptop)
           data.save()
        
           
    else:
        form=DjangoForm()
        print('get statement')
    return render(request,'first/showform.html', {'form':form})