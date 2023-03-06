from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)

        self.fields['email'].required = True


    #email validation, user validation is built in
    def clean_email(self):
        email = self.cleaned_data.get('email')

        #check if email already exists
        if User.objects.filter(email = email).exists():
            raise forms.ValidationError('Email taken')

        #check if length is very long
        if len(email) >= 350:
            raise forms.ValidationError('email too long')
        
        return email