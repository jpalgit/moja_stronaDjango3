from django.contrib import admin
from .models import Post
# admin.site.register(Post)


class PostyAdmina(admin.ModelAdmin):
    list_display = ('tytul', 'kategoria', 'data_utworzenia', 'data_publikacji', 'data_aktualizacji')
    prepopulated_fields = {'slug': ('tytul',)}
    list_filter = ('data_utworzenia', 'kategoria')
    search_fields = ('tytul', 'tresc')


admin.site.register(Post, PostyAdmina)   # rejestracja modelu Post
