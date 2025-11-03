from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm


def register(request):
    """
    Відображення сторінки реєстрації користувача.
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Акаунт {username} створено успішно!')
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register/register.html', {'form': form})
