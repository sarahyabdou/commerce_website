# myapp/urls.py

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),  # Maps the root URL to the index view
#     path('product/', views.product, name='product'),  # Maps the /about/ URL to the about view
#     # Add more URL patterns as needed
# ]
# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    
    path('product/', views.product_view, name='product'),
      path('product/<int:productid>',views.productdetails,name="product.details"),
    path('category/', views.category_view, name='category'),
     path('category/<int:categoryidc>',views.categorydetails,name="category.details"),
     
    path('about/', views.about_view, name='about'),
]

