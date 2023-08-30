from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import BaseUserRegistrationForm, SellerRegistrationFormSet, BuyerRegistrationFormSet, UserAuthenticationForm, SellerCardFormSet
from .models import UserAccount, BuyerAccount, SellerAccount, SellerCardDetail

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect("/account/userprofile")
        redirect()
    return render(request, "account/index.html")
        
def register_buyer(request):
    buyerform = BuyerRegistrationFormSet
    if request.method == "POST":
        user_register = BaseUserRegistrationForm(request.POST)
        if user_register.is_valid():
            user = user_register.save(commit=False)
            formset = buyerform(request.POST, instance = user)
            if formset.is_valid():
                formset.save()
                user_register.save()
                username = user_register.cleaned_data.get("username")
                password = user_register.cleaned_data.get("password1")
                account = authenticate(username=username, password=password)
                login(request, account)
                return redirect('/')
            else:
                print(formset.errors)
                formset = buyerform(instance = user)
        return render(request, 'account/register_buyer.html', {'registration_buyer':buyerform, 'registration_base':user_register})
    else:
        return render(request, 'account/register_buyer.html', {'registration_buyer':buyerform, 'registration_base':BaseUserRegistrationForm(request.GET)})

def register_seller(request):
    sellerform = SellerRegistrationFormSet
    if request.method == "POST":
        user_register = BaseUserRegistrationForm(request.POST)
        if user_register.is_valid():
            user = user_register.save(commit=False)
            formset = sellerform(request.POST, instance = user)
            if formset.is_valid():
                formset.save()
                user_register.save()
                username = user_register.cleaned_data.get("username")
                password = user_register.cleaned_data.get("password1")
                account = authenticate(username=username, password=password)
                login(request, account)
                return redirect('home')
            else:
                print(formset.errors)
                formset = sellerform(instance = user)
        return render(request, 'account/register_seller.html', {'registration_seller':sellerform, 'registration_base':user_register})
    else:
        return render(request, 'account/register_seller.html', {'registration_seller':sellerform, 'registration_base':BaseUserRegistrationForm(request.GET)})

def login_user(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("/account")

    if request.method == "POST":
        user_login = UserAuthenticationForm(request.POST)
        if user_login.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect("/account")

    else:
        user_login = UserAuthenticationForm(request.GET)

    context['user_login'] = user_login
    return render(request, "account/login.html", context)


def logout_user(request):
    logout(request)
    return redirect('/account')

@login_required(login_url="/account/")
def user_profile(request):
    cards = SellerCardDetail.objects.filter(seller_details__user=request.user)
    return render(request, "account/profile.html", {"cards": cards})

@login_required(login_url="/account/")
def add_seller_card(request):
    card_form = SellerCardFormSet
    user = SellerAccount.objects.get(user=request.user)
    if request.method == "POST":
        formset = card_form(request.POST, request.FILES, instance=user)
        print(formset)
        if formset.is_valid():
            formset.save()
            # TODO: don't immediately save a card, instead, get its name, 
            # query scryfall for it, give the user an option to choose from variations(if any)
            # then fill in the field for it
            return redirect("/")
        else:
            print(formset.errors)
            formset = card_form(instance=user)
        return render(request, 'account/profile/addcard.html', {"add_card": formset})
    else:
        return render(request, 'account/profile/addcard.html')