from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.forms import UsernameField


class LoginForm(forms.Form):
    username = UsernameField(
        label='ユーザ名',
        max_length=255,
    )
    password = forms.CharField(
        label='パスワード',
        strip=False,
        widget=forms.PasswordInput(render_value=True),
    )

    def __init__(self, *args):
        super().__init__(*args)

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) < 3:
            raise forms.ValidationError(
                '%(min_length)s 文字以上で入力してください', params={'min_length': 3}
            )
        return username

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            raise forms.ValidationError('正しいユーザ名を入力してください')
        if not user.check_password(password):
            raise forms.ValidationError('正しいユーザ名とパスワードを入力してください')

        self.user = user
