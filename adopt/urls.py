from django.urls import path
from adopt.controller import home
from adopt.controller import cart
from adopt.controller import categories
from adopt.controller import checkout
from adopt.controller import contact
from adopt.controller import product
from adopt.controller import register
from adopt.controller import admin
from django.conf.urls import url,include

urlpatterns = [
    url(r'^$',home.base,name="home"),
    url(r'^cart',cart.bag,name="cart"),
    url(r'^categories',categories.category,name="categories"),
    url(r'^checkout',checkout.purchase,name="checkout"),
    url(r'^contact',contact.contact,name="contact"),
    url(r'^product',product.prod,name="product"),
    url(r'^register',register.reg,name="register"),
    url(r'^admin',admin.admin,name="admin"),
]
