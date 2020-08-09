from django.contrib import admin
from django.urls import path
from quotes.views import home, about, add_stock, delete_stock

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name = "home"),
    path('about/', about, name = "about"),
    path('add_stock/', add_stock, name = "add_stock"),
    path('delete_stock/<str:stock_symbol>', delete_stock, name = "delete_stock"),
]
