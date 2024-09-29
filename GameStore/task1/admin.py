from django.contrib import admin
from .models import Game, Buyer


# Настройка админки для модели Game
class GameAdmin(admin.ModelAdmin):
    # Отображаемые поля в списке объектов
    list_display = ('title', 'cost', 'size', 'age_limited')
    # Поля, по которым можно искать
    search_fields = ('title', 'description')
    # Фильтрация по возрастным ограничениям и цене
    list_filter = ('age_limited', 'cost')
    # Сортировка по убыванию цены
    ordering = ('-cost',)


# Настройка админки для модели Buyer
class BuyerAdmin(admin.ModelAdmin):
    # Отображаемые поля в списке объектов
    list_display = ('name', 'balance', 'age')
    # Поля, по которым можно искать
    search_fields = ('name',)
    # Фильтрация по возрасту
    list_filter = ('age',)


# Регистрация моделей с настройками
admin.site.register(Game, GameAdmin)
admin.site.register(Buyer, BuyerAdmin)
