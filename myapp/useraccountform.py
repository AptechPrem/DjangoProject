from .models import *
from django import forms


 
class useraccountform(forms.ModelForm):
  firstName=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'}))
  lastName=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last Name'}))
  emailAddress=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email Address'}))
  password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter the Password'}))
  class Meta:
    model=userAccount
    fields=['firstName','lastName','emailAddress','password']

 

class CustomUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user