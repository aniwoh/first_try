from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core import validators
from django.contrib.auth.models import User
from django.contrib.auth import password_validation

class UserRegistrationForm(UserCreationForm):
    # 自定义用户名字段
    username = forms.CharField(
        label="用户名", 
        max_length=10,
        widget=forms.TextInput(attrs={'placeholder': '用户名'}),
        error_messages={
            'unique': '该用户名已存在。请使用其他用户名。'
        },)
    # 自定义密码字段
    password1 = forms.CharField(
        label="密码",
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': '密码至少8个字符'}),
        validators=[
            validators.MinLengthValidator(limit_value=8, message="密码长度至少为8个字符。"),
            validators.RegexValidator(
                regex=r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).*$',
                message="密码必须包含大小写字母和数字。",
                code="invalid_password"
            )
        ]
    )

    password2 = forms.CharField(
        label="确认密码",
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': '再次输入密码'}),
        validators=[password_validation.validate_password]
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
