from django.contrib import admin

from burgers.models import Burger


# Register your models here.

# 관리자 계정 설정
#

@admin.register(Burger)
class BurgerAdmin(admin.ModelAdmin):
    pass
