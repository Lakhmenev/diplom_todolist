from core.models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Настройка админки пользователя"""

    # Отображаемые поля
    list_display = ('username', 'email', 'first_name', 'last_name')
    # Поля для фильтров
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    # Поля для осуществления поиска
    search_fields = ('email', 'first_name', 'last_name', 'username')
    # Исключаемые из админки поля
    # exclude = ['password']
    # Поля только для чтения
    readonly_fields = ('last_login', 'date_joined')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (
            'Personal Info',
            {'fields': ('first_name', 'last_name', 'email')}
        ),
        (
            'Permission',
            # {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups')}
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (
            'Important dates',
            {'fields': ('last_login', 'date_joined')}
        )
    )

    def get_list_display(self, request):
        default_list_display = super(UserAdmin, self).get_list_display(request)
        if request.user.is_superuser:
            default_list_display = ('username', 'email', 'last_name', 'first_name', 'password')
        return default_list_display


# Меняем заголовок админки
admin.site.site_title = 'Администрирование ToDoList'
admin.site.site_header = 'Администрирование ToDoList'
