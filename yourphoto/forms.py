from django import forms

from yourphoto.models import Users


class Registration(forms.Form):
    OPTIONS = [('YS', 'I`m a photographer'),
               ('NS', ' I`m not a photographer')]
    status = forms.ChoiceField(choices=OPTIONS, widget=forms.RadioSelect(attrs={'name': 'status'}))
    full_name = forms.CharField(min_length=5, widget=forms.TextInput(attrs={'name': 'full_name'}))
    phone = forms.CharField(min_length=5, widget=forms.TextInput(attrs={'name': 'phone'}))
    city = forms.CharField(min_length=3, widget=forms.TextInput(attrs={'name': 'city'}))
    email = forms.EmailField(min_length=5, widget=forms.EmailInput(attrs={'name': 'email'}))
    login = forms.CharField(min_length=5, widget=forms.TextInput(attrs={'name': 'login'}))
    password = forms.CharField(min_length=5, widget=forms.PasswordInput(attrs={'name': 'password'}))


class Auth(forms.Form):
    login = forms.CharField(min_length=5, widget=forms.TextInput(attrs={'name': 'login'}))
    password = forms.CharField(min_length=5, widget=forms.PasswordInput(attrs={'name': 'password'}))


class Filter_form(forms.Form):
    cities = list(set((item.city, item.city) for item in Users.objects.all().distinct()))
    city = forms.ChoiceField(choices=cities, widget=forms.Select(attrs={'name': 'select'}))

class PanelUpdate(forms.Form):
    OPTIONS = [('YS', 'I`m a photographer'),
               ('NS', ' I`m not a photographer')]
    status = forms.ChoiceField(choices=OPTIONS, widget=forms.RadioSelect(attrs={'name': 'status', "id": "status"}))
    full_name = forms.CharField(min_length=5, widget=forms.TextInput(attrs={'name': 'full_name', "id": "full_name"}))
    phone = forms.CharField(min_length=5, widget=forms.TextInput(attrs={'name': 'phone', "id": "phone"}))
    city = forms.CharField(min_length=3, widget=forms.TextInput(attrs={'name': 'city', "id": "city"}))
    email = forms.EmailField(min_length=5, widget=forms.EmailInput(attrs={'name': 'email', "id": "email"}))
    login = forms.CharField(min_length=5, widget=forms.TextInput(attrs={'name': 'login', "id": "login"}))
    password = forms.CharField(min_length=5, widget=forms.PasswordInput(attrs={'name': 'password', "id": "password"}))
