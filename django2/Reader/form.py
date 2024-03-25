from django import forms


class user_form(forms.Form):
    user_name =  forms.CharField(label="name",max_length=100,required=True)
    user_password =  forms.CharField(label="password",max_length=100,required=True)
    