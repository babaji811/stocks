import requests
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Stock

def home(request):

    if request.method == 'GET':
        msg = 'Type in company symbol above to get quote!'
        return render(request, 'home.html', {'msg': msg})
    else:
        symbol = (request.POST['symbol']).upper()
        api_request = requests.get(f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote?token=Tpk_6aa25db23c2a47dc87cbc74842c86de8')
        
        try:
            api = api_request.json()
        except Exception as e:
            api = 'Error'

        return render(request, 'home.html', {'api': api})

def about(request):
    return render(request, 'about.html', {})

def add_stock(request):
    if(request.method == 'GET'):
        api_list = []
        symbols = Stock.objects.all()
        
        for symbol in symbols:
            api_request = requests.get(f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote?token=Tpk_6aa25db23c2a47dc87cbc74842c86de8')
            
            try:
                api = api_request.json()
                api_list.append(api)
            except Exception as e:
                api = 'Error'
        
        return render(request, 'add_stock.html', {'symbols': symbols, 'api_list': api_list })
    else:
        companySymbol = (request.POST['companySymbol']).lower()
        obj = Stock.objects.filter(symbol=companySymbol).first()
        if(obj is None):
            companyStock = Stock(symbol=companySymbol)
            companyStock.save()
            messages.success(request, ('Stock added successfully!'))
            return redirect('/add_stock/')
        else:
            messages.error(request, ('Stock already exists in database.'))
            return redirect('/add_stock/')

def delete_stock(request, stock_symbol):
    stock = Stock.objects.get(symbol=stock_symbol.lower())
    stock.delete()
    messages.success(request, ('Stock deleted successfully!'))
    return redirect('/add_stock/')