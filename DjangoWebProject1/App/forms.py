from cProfile import label
from msilib.schema import CheckBox
from django import forms
from phonenumber_field.formfields import PhoneNumberField
from django_countries.fields import CountryField
from utilities.readyValues import *
from .models import Profile
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"

    Kyrgyz_som = forms.DecimalField(
        required=True,
        widget=forms.NumberInput(attrs={"id": "currencyA", "name": "currencyA", "oninput": "callTwoFunctions('A', this.value)"})
    )    
    USD = forms.DecimalField(
        required=True,
        widget=forms.NumberInput(attrs={"id": "currencyB", "name": "currencyB", "oninput": "callTwoFunctions('B', this.value)"})
    )
    Euro = forms.DecimalField(
        required=True,
        widget=forms.NumberInput(attrs={"id": "currencyC", "name": "currencyC", "oninput": "callTwoFunctions('C', this.value)"})
    )
 
    Confirm_Email = forms.EmailField(required=True)
    First_name = forms.CharField(max_length=20, required=True)
    Last_name = forms.CharField(max_length=40, required=True)
    Phone_number = PhoneNumberField()
    Country = CountryField(blank_label='Select Country').formfield()
    
    Connection = forms.CharField(
        max_length=50,
        widget=forms.Select(choices=ReadyConnetions),
        required=False
       )
    Fund = forms.CharField(
        max_length=60,
       widget=forms.Select(choices=ReadyFundPriories), 
       required=False
       )
    Inspired = forms.CharField(
       widget=forms.Textarea(attrs={"id":"Inspired","rows":"3","placeholder":"What inspired you to give today's gift to the AUCA Fund/Alumni Fund?"}),
       max_length=200, 
       required=False
       )
    Comments = forms.CharField(
        widget=forms.Textarea(attrs={"id":"Comment","rows":"2","placeholder":"Comments"}),
       max_length=100, 
       required=False)
    Offer= forms.BooleanField(widget=forms.CheckboxInput(attrs={"id":"offer"}))