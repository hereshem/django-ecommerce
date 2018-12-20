
from django.urls import path

from shop import views

app_name = "shop"

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('signout/', views.signout, name="signout"),
    path('search/', views.search, name="search"),
    path('<slug>/cart/', views.cart, name="cart"),
    path('mycart/', views.mycart, name="cart"),
    path('checkout/', views.checkout, name="cart"),

    path('<slug>/', views.detail, name="detail"),

    path('categories/<slug>/', views.categories, name="categories"),
]