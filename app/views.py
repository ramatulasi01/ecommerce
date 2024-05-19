from django.shortcuts import render

from app.models import Product

# Create your views here.
def index(request):
    data=Product.objects.all()
    context={"data":data}
    return render(request,"index.html",context)
def about(request):
    return render(request,"about.html")
def insertdata(request):
    if request.method=="POST":
        name=request.POST.get('name')
        id=request.POST.get('id')
        price=request.POST.get('price')
        query=Product(name=name,id=id,price=price)
        query.save()
    return render(request,"index.html")