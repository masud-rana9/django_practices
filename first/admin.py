

# Register your models here.
from django.contrib import admin
from .models import Payment,modelForm
class paymethod(admin.ModelAdmin):
    list_display=('id','user','amount','payment_date','payment_method','status')
admin.site.register(Payment, paymethod)




class modelfromre(admin.ModelAdmin):
    list_display=('mobile','laptop')
admin.site.register(modelForm, modelfromre)