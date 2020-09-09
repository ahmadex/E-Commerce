from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import *
from math import ceil
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request):

    # product = Product.objects.all()
    # n = len(product)
    # nslide = n//4+ceil((n/4)-(n//4))

    # all_prod = [[product,range(1,nslide),nslide],
    #             [product,range(1,nslide),nslide]]
    all_prod = []
    cat_prod = Product.objects.values('category','id')
    cats = {item['category'] for item in cat_prod}

    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nslides = n//4 + ceil((n/4)-(n//4))
        all_prod.append([prod,range(1,nslides), nslides])

    context = {'allprod':all_prod}
    return render(request,'ecom/a.html',context)

def index(request):
    return render(request,'ecom/index.html')


def product(request,pk):
    prod = Product.objects.get(id=pk)
    return render(request,'ecom/product.html', {'prod':prod})

def contact_us(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile_no = request.POST.get('mobile_no',)
        query = request.POST.get('query')
        print(name,email,mobile_no,query)
        contact = ContactUs(name=name, phone_no=mobile_no, email=email , query=query)
        contact.save()

    return render(request,'ecom/contact_us.html')


def checkout(request):

    if request.method == 'POST':
        itemjson = request.POST.get('itemjson')
        amount = request.POST.get('amount')
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get("adress1")
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        phone_no = request.POST.get('phone_no')

        order = Order(item_json=itemjson, amount=amount, name=name, email=email, address=address, city=city, state=state, zipcode=zip, phone_no=phone_no)
        order.save()
        update = OrderUpdate(order_id=order.id, update_desc='The Order Has Benn Placed!!')
        update.save()
        thank = True
        id = order.id
        return render(request,'ecom/checkout.html', {'thank':thank, 'id':id})
    return render(request,'ecom/checkout.html')

@csrf_exempt
def handlerequest(request):
    pass


def tracker(request):

    if request.method == 'POST':
        orderid = request.POST.get('orderid')
        email = request.POST.get('email')
        try:
            order = Order.objects.filter(id=orderid, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderid)
                updates = []
                for item in update:
                    updates.append({'text':item.update_desc, 'time':item.timestamp})
                    response = json.dumps([updates,order[0].item_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request,'ecom/tracker.html')
