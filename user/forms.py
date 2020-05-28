from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label = "user name")
    password = forms.CharField(label = "pasward",widget = forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length = 50,label = "user name")
    password = forms.CharField(max_length=20,label = "Passward",widget = forms.PasswordInput)
    confirm = forms.CharField(max_length=20,label ="confirm passward",widget = forms.PasswordInput)
    
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("confirm password")

        values = {
            "username" : username,
            "password" : password
        }
        return values


