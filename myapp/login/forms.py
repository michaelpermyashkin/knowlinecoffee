from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class SignUpForm(UserCreationForm):        
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.pop("autofocus", None)

    first_name = forms.CharField(max_length=30, required=True, 
        widget=forms.TextInput(attrs={'placeholder': 'First name'})
    )
    username = forms.CharField(max_length=30, required=True, 
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    email = forms.EmailField(max_length=254, required=True, 
        widget=forms.TextInput(attrs={'placeholder': 'email@example.com'})
    )
    password1 = forms.CharField(max_length=254, required=True, 
        widget=forms.TextInput(attrs={'placeholder': 'Enter password', 'type': 'password'})
        
    )
    password2 = forms.CharField(max_length=254, required=True, 
        widget=forms.TextInput(attrs={'placeholder': 'Confirm password', 'type': 'password'})
    )
    
    class Meta:
        model = User
        fields = ('first_name', 'username', 'email', 'password1', 'password2')
 

class UsersLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget = forms.PasswordInput)

	def __init__(self, *args, **kwargs):
		super(UsersLoginForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({
		    'class': 'form-control',
		    "name":"username",
			'placeholder': 'Username',
			'type': 'text'})
		self.fields['password'].widget.attrs.update({
		    'class': 'form-control',
		    "name":"password",
			'placeholder': 'Password',
			'type': 'password'})



	def clean(self, *args, **keyargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")

		if username and password:
			user = authenticate(username = username, password = password)
			if not user:
				raise forms.ValidationError("This user does not exists")
			if not user.check_password(password):
				raise forms.ValidationError("Incorrect Password")
			if not user.is_active:
				raise forms.ValidationError("User is no longer active")

		return super(UsersLoginForm, self).clean(*args, **keyargs)