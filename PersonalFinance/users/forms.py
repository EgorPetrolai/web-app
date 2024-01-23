from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'userform'
        self.fields['email'].widget.attrs['class'] = 'userform'
        self.fields['password1'].widget.attrs['class'] = 'userform'
        self.fields['password2'].widget.attrs['class'] = 'userform'

class SignInForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'userform'
        self.fields['password'].widget.attrs['class'] = 'userform'
