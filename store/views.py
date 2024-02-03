
from django.shortcuts import render
from django.http import  HttpResponse

products = [
        {'id': 1, 'name': 'Product 1', 'details': 'Product 1 details'},
        {'id': 2, 'name': 'Product 2', 'details': 'Product 2 details'},
        {'id': 3, 'name': 'Product 3', 'details': 'Product 3 details'},
        {'id': 4, 'name': 'Product 4', 'details': 'Product 4 details'},
        {'id': 5, 'name': 'Product 5', 'details': 'Product 5 details'},
        {'id': 6, 'name': 'Product 6', 'details': 'Product 6 details'},
        {'id': 7, 'name': 'Product 7', 'details': 'Product 7 details'},
        {'id': 8, 'name': 'Product 8', 'details': 'Product 8 details'},
        {'id': 9, 'name': 'Product 9', 'details': 'Product 9 details'},
    ]
def product_view(request):
    # Fetch product data from your desired source and organize it as a list

    return render(request, 'product.html', {'products': products})

categories = [
        {'idc': 1, 'namec': 'mask', 'detailsc': 'category 1 details','path': 'pro1.jpg'},
        {'idc': 2, 'namec': 'osea', 'detailsc': 'category 2 details','path': 'pro2.jpg'},
       
         {'idc': 3, 'namec': 'loreal', 'detailsc': 'category 3 details','path': 'pro3.jpg'},
        {'idc': 4, 'namec': 'category 4', 'detailsc': 'category 4 details','path': 'pro10.jpg'},
        {'idc': 5, 'namec': 'sheglam blush', 'detailsc': 'category 5 details','path': 'pro5.jpg'},
          {'idc': 6, 'namec': 'ice roller', 'detailsc': 'category 6 details','path': 'pro6.jpg'},
        {'idc': 7, 'namec': 'oil', 'detailsc': 'category 7 details','path': 'pro7.jpg'},
        {'idc': 8, 'namec': 'tanasha', 'detailsc': 'category 8 details','path': 'pro8.jpg'},
        {'idc': 9, 'namec': 'mac blusher', 'detailsc': 'category 9 details','path': 'pro9.jpg'},
    ]
def category_view(request):
   
    
  
    return render(request, 'category.html', {'categories': categories})


def about_view(request):
    return render(request, 'about.html')

def categorydetails(request,categoryidc):
   
    category=filter(lambda c:c['idc']==categoryidc,categories )
    
    category=list(category)
    if category:
        return HttpResponse(category)
def productdetails(request,productid):
   
    product=filter(lambda p:p['id']==productid,products )
    
    product=list(product)
    if product:
        return HttpResponse(product)
    



    


