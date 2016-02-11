from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response

from .models import Product
import datetime
from django.utils import timezone

def index(request):

    if request.method == 'POST':
        p = Product(
            product_text=request.POST.get('name'),
            product_desc=request.POST.get('desc'),
            pub_date=timezone.now()
            )
        p.save()
        return HttpResponseRedirect("/product/")
    else:
        product_list = Product.objects.order_by('-pub_date')
        context = {'product_list': product_list , 'message':'success'}
        return render(request,'products/index.html', context )


def update(request,id):

    if request.method == 'POST':
        p = Product.objects.get(pk = id)
        p.product_text = request.POST.get('name')
        p.product_desc = request.POST.get('desc')
        p.save()
        return HttpResponseRedirect("/product/")
    else:
        product = Product.objects.get(pk = id)
        context = {'product_list': product , 'message':'success'}
        return render(request,'products/edit.html', context )


def delete(request, id):
   p = Product.objects.get(pk = id)
   p.delete()
   return HttpResponseRedirect("/product/")
