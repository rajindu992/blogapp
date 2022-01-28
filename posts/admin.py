from django.contrib import admin
from .models import Article, Profile


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'image', 'created_on')
    list_filter = ("title",)
    search_fields = ['title', 'body']



admin.site.register(Article, ArticleAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'image', 'gender')
    list_filter = ("user",)
    search_fields = ['user']


admin.site.register(Profile, ProfileAdmin)