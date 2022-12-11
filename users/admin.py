from django.contrib import admin
from .models import Users, Cargo
from django.contrib.auth import admin as admin_auth_django
from .forms import UserChangeForm, UserCreationForm

admin.site.register(Cargo)

@admin.register(Users)
class UsersAdmin(admin_auth_django.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = Users
    fieldsets = admin_auth_django.UserAdmin.fieldsets + (
        ('Cargo', {'fields': ('cargo',)}), 
        ('Cpf', {'fields': ('cpf',)}), 
        ('Data de nascimento', {'fields': ('data_nascimento',)})
        ,)  # type: ignore
    