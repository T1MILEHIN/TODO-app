from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Django_Created_Form(UserCreationForm):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Enter Your First name'
    }))
    last_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':"Your Last Name",
    }))
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder': "Please enter your Email Address."
    }))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


    def __init__(self, *args, **kwargs):
        super(Django_Created_Form, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter Your Username'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter Your Password'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'













def __init__(self, *args, **kwargs):
    super(Django_Created_Form, self).__init__(*args, **kwargs)

    























