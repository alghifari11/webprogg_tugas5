from django import forms
from shaura.models import AccountUser

class StudentRegisterForm(forms.ModelForm):
    fullname = forms.CharField(max_length=255)
    nim = forms.CharField(max_length=20)
    email = forms.EmailField()

    class Meta:
        model = AccountUser
        fields = ['fullname', 'nim', 'email']
