from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core import validators
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    # 自定义用户名字段
    username = forms.CharField(
        label="用户名",  # 前端通过{{form.username.label_tag}}调用
        max_length=10,
        widget=forms.TextInput(attrs={'placeholder': '用户名'}),
        error_messages={
            'unique': '该用户名已存在。请使用其他用户名。',
            'equired': '用户名不能为空!'
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
    )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("密码不匹配")


    class Meta:
        model = User
        fields = ('username', 'password1','password2')
