from django.shortcuts import render, redirect, get_object_or_404
from .models import Home
from realtors.models import Realtor
from django.db.models import Q
from django.core.paginator import PageNotAnInteger, Paginator,EmptyPage
from django.contrib import messages
# Create your views here.
def Test(request):
    homes = Home.objects.order_by('-list_date').filter(status = 'published')[:3]
    context = {
        'homes':homes,
    }
    return render(request, 'myApp/index.html', context)

def About(request):
    # get all realtors
    realtors = Realtor.objects.order_by('-hire_date') 

    #get the mvp realtor 
    mvp_realtors = Realtor.objects.filter(is_mvp = True)

    context = {
        'realtors':realtors,
        'mvp_realtors':mvp_realtors
    }


    return render(request, 'myApp/about.html', context)

def Detail(request, id):
    home = get_object_or_404(Home, id=id)

    # show random 3 houses from same city 
    # this will loop through the houses with same location of above home and exclude the above home
    homes = Home.homes.order_by('?').filter(district = home.district).exclude(id=id)[:3]   
    
    context = {
        'home':home,
        'homes':homes,
    }
    return render(request, 'myApp/detail.html', context)

def Listing(request):
    homes_list = Home.homes.all().order_by('-id')
    paginator = Paginator(homes_list,6)
    page  = request.GET.get('page')
    
    try:
        homes = paginator.page(page)
    except PageNotAnInteger:
        homes = paginator.page(1)
    except EmptyPage:
        homes = paginator.page(paginator.num_pages)
    
    # To show limited number of paginatior number 
    if page is None:
        start_index = 0
        end_index  = 7
    else:
        (start_index, end_index) = Proper_paginator(homes, index=4)
    
    page_range = list(paginator.page_range)[start_index:end_index]


    context = {
        'homes':homes,
        'page_range':page_range,
    }
    return render(request, 'myApp/list.html',context)

def Proper_paginator(homes, index):
    start_index = 0
    end_index = 7
    if homes.number > index:
        start_index = homes.number - index
        end_index   = homes.number + index
    return (start_index, end_index)

def SearchView(request):
    if request.GET.get('keywords'):
        keyword = request.GET['keywords'] 
        search_result = Home.homes.filter(description__icontains = keyword)
    
    if request.GET.get('city'):
        city = request.GET['city']
        search_result = Home.homes.filter(city__icontains = city)
    
    if request.GET.get('district'):
        district = request.GET['district']
        search_result = Home.homes.filter(district__icontains = district)
    
    if request.GET.get('bedrooms'):
        bedroom = request.GET['bedrooms']
        search_result = Home.homes.filter(bedroom__lte = bedroom)
    
    if request.GET.get('price'):
        price = request.GET['price']
        search_result = Home.homes.filter(price__lte = price)
    
    context = {
        'homes':search_result,
        'values':request.GET, # this helps to preserve data in search.html form;
    }

    return render(request, 'myApp/search.html',context)




        
