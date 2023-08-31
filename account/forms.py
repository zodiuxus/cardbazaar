from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate

from .models import UserAccount, BuyerAccount, SellerAccount, SellerCardDetail

class BaseUserRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=250, required=True)
    full_name = forms.CharField(max_length=50, required=True)
    phone = forms.IntegerField(required=False)

    class Meta:
        model = UserAccount
        fields = ("username", "email", "full_name", "phone", "password1", "password2")

class SellerCardBase(forms.BaseInlineFormSet):
    def clean(self):
        if not self.has_changed():
            raise forms.ValidationError('I have no idea what went wrong, but I know this error is here')

BuyerRegistrationFormSet = inlineformset_factory(UserAccount, BuyerAccount, fields=('shipping_address', 'billing_address',))

SellerRegistrationFormSet = inlineformset_factory(UserAccount, SellerAccount, fields=('swift_code_transaction',))

SellerCardFormSet = inlineformset_factory(SellerAccount, SellerCardDetail, fields=('card_name', 'card_quality', 'card_price', 'card_notes', 'card_stock'), formset=SellerCardBase)

class UserAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    class Meta:
        model = UserAccount
        fields = ("username", "password")

    def clean(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            if not authenticate(username=username, password=password):
                raise forms.ValidationError("Invalid credentials. Try again.")
