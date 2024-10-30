from django.urls import path
from . import views
from .views import cart, add_to_cart
from .views import CreateView

urlpatterns = [
    
    path('', CreateView.as_view(), name='Create'),
    
    path('cart/',cart, name='cart'),
    
    path('product/',views.product, name='product'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('footer/', views.product, name='footer'),
    
    
]
