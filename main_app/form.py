# from django.forms import forms

from django import forms
from django.contrib.auth.forms import UserCreationForm


from main_app.models import Login, Donor, Receiver, Receiver_Request, Feedback


class LoginForm(UserCreationForm):
    username =forms.CharField()
    password1 = forms.CharField(label='password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password',widget=forms.PasswordInput)


    class Meta:
        model = Login
        fields = ('username','password1','password2')


class DonorRegister(forms.ModelForm):
    class Meta:
        model = Donor
        fields ="__all__"
        exclude =("user",)

class ReceiverRegister(forms.ModelForm):
    class Meta:
        model =Receiver
        fields ="__all__"
        exclude =("user",)

class DateInput(forms.DateInput):
    input_type = 'date'

class ReceiverRequest(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model =Receiver_Request
        fields ="__all__"
        exclude =("Receiver_name","Donor_name",)

class Fdbk(forms.ModelForm):
    class Meta:
        model =Feedback
        fields ="__all__"
        exclude =("Receiver_name","date","Replay",)
