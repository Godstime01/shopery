from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CUser
from django import forms

class AccountCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        for visible in self.visible_fields():
            
            visible.field.widget.attrs['class'] = 'rounded-md w-full shadow border block my-2'
            visible.field.widget.attrs['placeholder'] = visible.field.label
            visible.label_tag(attrs={'class': 'text-purple-400 mb-5'})

    class Meta:
        model = CUser
        fields = ['email', 'password1', 'password2']
    


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            
            visible.field.widget.attrs['class'] = 'rounded-md w-full shadow border block my-2'
            visible.field.widget.attrs['placeholder'] = visible.field.label
            visible.label_tag(attrs={'class': 'text-purple-400 mb-5'}) 

    class Meta:
        model = CUser
        fields = '__all__'