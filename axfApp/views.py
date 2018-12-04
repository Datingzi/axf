from django.shortcuts import render
from django.http import HttpResponse
from axfApp.models import Product, Category, ChildCategory


# Create your views here.


def index(request):
    return render(request, "axfApp/base/base.html")


def home(request):
    return render(request, "axfApp/home/home.html")


def market(request, categoryId, childId, sortId):
    # 获取分组数据
    categories = Category.objects.all()
    # 获取子组数据
    childCategories = ChildCategory.objects.filter(category__categoryId=categoryId)
    # 获取商品数据
    products = Product.objects.filter(categoryId=categoryId)
    if childId != "0":
        products = Product.objects.filter(childCid=childId)
    # 获取分类的数据,几个升序，价格降序
    if sortId == "1":
        products = products.order_by("-price")
    elif sortId == "2":
        products = products.order_by("price")
    return render(request, "axfApp/market/market.html",
                  {"categories": categories, "products": products, "childCategories": childCategories,
                   "gid": categoryId, "childGid": childId})


def cart(request):
    return render(request, "axfApp/cart/cart.html")


def mine(request):
    return render(request, "axfApp/mine/mine.html")
