
from django.shortcuts import render

def product_view(request):
    # Fetch product data from your desired source and organize it as a list
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
    return render(request, 'product.html', {'products': products})


def category_view(request):
   
    categories = [
        {'idc': 1, 'namec': 'category 1', 'detailsc': 'category 1 details','image': 'category1.jpg'},
        {'idc': 2, 'namec': 'category 2', 'detailsc': 'category 2 details','image': 'category2.jpg'},
       
         {'idc': 3, 'namec': 'category 3', 'detailsc': 'category 3 details','image': 'category3.jpg'},
        {'idc': 3, 'namec': 'category 4', 'detailsc': 'category 4 details','image': 'category4.jpg'},
        {'idc': 5, 'namec': 'category 5', 'detailsc': 'category 5 details','image': 'category5.jpg'},
          {'idc': 6, 'namec': 'category 6', 'detailsc': 'category 6 details','image': 'category6.jpg'},
        {'idc': 7, 'namec': 'category 7', 'detailsc': 'category 7 details','image': 'category7.jpg'},
        {'idc': 8, 'namec': 'category 8', 'detailsc': 'category 8 details','image': 'category8.jpg'},
        {'idc': 9, 'namec': 'category 9', 'detailsc': 'category 9 details','image': 'category9.jpg'},
    ]
    return render(request, 'category.html', {'categories': categories})
def about_view(request):
    return render(request, 'about.html')
