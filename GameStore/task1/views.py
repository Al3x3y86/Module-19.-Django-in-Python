from django.shortcuts import render
from .forms import UserRegister
from .models import Buyer
from .models import Game


def main_page(request):
    return render(request, 'fourth_task/platform.html')


def shop_page(request):
    games = Game.objects.all()
    return render(request, 'fourth_task/games.html', {'games': games})


def cart_page(request):
    return render(request, 'fourth_task/cart.html')


users = ['testuser']


def sign_up_by_django(request):
    info = {}

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            # Проверяем, существует ли пользователь с таким именем в таблице Buyer
            if Buyer.objects.filter(name=username).exists():
                info['error'] = 'Пользователь с таким именем уже существует'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            else:
                # Добавляем нового покупателя в таблицу Buyer
                Buyer.objects.create(name=username, balance=0, age=age)
                return render(request, 'fifth_task/registration_page.html', {'message': f'Приветствуем, {username}!'})

    else:
        form = UserRegister()

    return render(request, 'fifth_task/registration_page.html', {'form': form, 'error': info.get('error', '')})
