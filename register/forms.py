from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label="Ім'я користувача",
        help_text="Обов'язково. Не більше 150 символів. Літери, цифри та @/./+/-/_",
        error_messages={'required': 'Будь ласка, введіть ім’я користувача.'}
    )
    email = forms.EmailField(
        label="Електронна пошта",
        help_text="Введіть дійсну адресу електронної пошти.",
        error_messages={'required': 'Це поле обов’язкове.'}
    )
    age = forms.IntegerField(label="Вік", required=False, initial=40)
    gender = forms.ChoiceField(
        label="Стать",
        required=False,
        choices=[("1", "чоловік"), ("2", "жінка")]
    )

    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput,
        help_text=(
            "Пароль має містити щонайменше 8 символів та не може складатися лише з цифр."
        )
    )

    password2 = forms.CharField(
        label="Підтвердження пароля",
        widget=forms.PasswordInput,
        help_text="Введіть той самий пароль ще раз для підтвердження."
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'age', 'gender')
