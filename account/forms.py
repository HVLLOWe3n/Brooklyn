from django.forms import ModelForm

from account.models import User


class UserForms(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name',
                  'last_name', 'avatar',
                  'password', 'email')
