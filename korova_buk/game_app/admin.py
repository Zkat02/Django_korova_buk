from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.

from game_app.models import BaseWords

class BaseWords_Admin(admin.ModelAdmin):
    list_display = ('id','base_word')
    search_fields = ('base_word',)
admin.site.register(BaseWords, BaseWords_Admin)