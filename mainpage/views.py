from django.shortcuts import render
from account.models import SellerCardDetail

# Create your views here.

def index(request):
    cards = SellerCardDetail.objects.order_by("-date_added")[:30]
    context = {"latest_cards_list": cards}
    return render(request, "mainpage/index.html", context)
