from django.urls import path
from . import views

urlpatterns = [
    path('', views.Brunc_idex, name='Brunc_idex'),
    path('user_register', views.userreg, name='userreg'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('user_login', views.user_login, name='user_login'),
    path('about_brunch', views.about_brunch, name='about_brunch'),
    path('contact_brunch', views.contact_brunch, name='contact_brunch'),
    path('brunchcarts/<int:id>', views.add_tocart, name='add_tocart'),
    path('getcartdetails', views.getcartdetails, name='getcartdetails'),
    path('viewcart_brunch', views.viewcart_brunch, name='viewcart_brunch'),
    path('cart_checkout', views.makepayment, name='makepayment'),
    path('brunchfilter/<str:fo_type>', views.brunchfilter, name='brunchfilter'),
    path('getfocnt', views.getfocnt, name='getfocnt'),
]