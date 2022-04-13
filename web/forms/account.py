from django import forms
from web import models


class RegisterModelForm(forms.ModelForm):

    password = forms.CharField(label='password', widget=forms.PasswordInput)
    confirmed_password = forms.CharField(label='confirm password', widget=forms.PasswordInput)
    code = forms.CharField(label='code')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = f'Input {field.label}'

    class Meta:
        model = models.User
        fields = '__all__'

