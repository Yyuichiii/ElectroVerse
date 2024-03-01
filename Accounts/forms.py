from django import forms
from .models import User,Address
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import password_validation




class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class": "form-control",'placeholder': 'Enter the Password'}))
    password2 = forms.CharField(
        label="Confirm Password", widget=forms.PasswordInput(attrs={"class": "form-control",'placeholder': 'Enter the Password'})
    )

    class Meta:
        model = User
        fields = ["email", "name","phone","password1","password2"]
        labels = {'email': 'Email Address',}
        widgets = {'email': forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Enter the Email'}),'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter the Name',}),'phone': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter the Phone Number',})}

    def clean_password2(self):
        print("m ismey aaya")
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Password and Confirm Password didn't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """

    class Meta:
        model = User
        fields = ["name", "phone"]
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter the Name',}),'phone': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter the Phone Number',})}


# login form
        

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        }
        labels = {
            'email': 'Email Address',
            'password': 'Password',
        }

    error_messages = {
        "invalid_login": _(
            "Please enter the correct email/password. Note that both "
            "fields may be case-sensitive."
        ),
        "inactive": _("This account is inactive."),}
    def get_invalid_login_error(self):
        return ValidationError(self.error_messages["invalid_login"],code="invalid_login",)
        
        
    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        self.user_cache = authenticate(username=email, password=password)
            
        if self.user_cache is None:
            raise self.get_invalid_login_error()
        


#Password Change Form
class Password_change_form(PasswordChangeForm):
    new_password1 = forms.CharField(label=_("New password"),widget=forms.PasswordInput(attrs={"class": "form-control" ,"placeholder": "Enter your new password here"}),strip=False,help_text=password_validation.password_validators_help_text_html(),)
    
    new_password2 = forms.CharField(
        label=_("Confirm New Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password","class": "form-control","placeholder": "Enter your new confirm password here"}),)

    old_password = forms.CharField(label=_("Old Password"),strip=False,widget=forms.PasswordInput(attrs={"autocomplete": "current-password", "autofocus": True,"class": "form-control","placeholder": "Enter your old password here"}))


# Address Form
class Address_form(forms.ModelForm):
    
    class Meta:
        model = Address
        exclude = ('user',)

        STATE_CHOICES = (
                ('', 'Select the State'),
                ('Andhra Pradesh', 'Andhra Pradesh'),
                ('Arunachal Pradesh', 'Arunachal Pradesh'),
                ('Assam', 'Assam'),
                ('Bihar', 'Bihar'),
                ('Chhattisgarh', 'Chhattisgarh'),
                ('Goa', 'Goa'),
                ('Gujrat', 'Gujrat'),
                ('Haryana', 'Haryana'),
                ('Himachal Pradesh', 'Himachal Pradesh'),
                ('Jharkhand', 'Jharkhand'),
                ('Karnataka', 'Karnataka'),
                ('Kerela', 'Kerela'),
                ('Madhya Pradesh', 'Madhya Pradesh'),
                ('Maharastra', 'Maharastra'),
                ('Manipur', 'Manipur'),
                ('Meghalaya', 'Meghalaya'),
                ('Mizoram', 'Mizoram'),
                ('Nagaland', 'Nagaland'),
                ('Odisha', 'Odisha'),
                ('Punjab', 'Punjab'),
                ('Rajasthan', 'Rajasthan'),
                ('Sikkim', 'Sikkim'),
                ('Tamil Nadu', 'Tamil Nadu'),
                ('Telengana', 'Telengana'),
                ('Tripura', 'Tripura'),
                ('Uttarakhand', 'Uttarakhand'),
                ('Uttar Pradesh', 'Uttar Pradesh'),
                ('West Bengal', 'West Bengal'),
                )

        widgets = {
            'Name': forms.TextInput(attrs={
                'class': 'form-control',
                "placeholder": "Enter your Name here"
                }),
            'Phone': forms.TextInput(attrs={
                'class': 'form-control',
                "placeholder": "Enter your Phone here"
                }),
            'Pincode': forms.TextInput(attrs={
                'class': 'form-control',
                "placeholder": "Enter your Pincode here"

                }),
            'State': forms.Select(choices=STATE_CHOICES,attrs={
                'class': 'form-control',
                "placeholder": "Select your State"
                }),
            'Street_Address': forms.TextInput(attrs={
                'class': 'form-control',
                "placeholder": "Enter your Street Address here",
                
                }),
            'Landmark': forms.TextInput(attrs={
                'class': 'form-control',
                "placeholder": "Enter your Landmark here"
                }),}
