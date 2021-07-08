from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _


from .models import CustomUser, Tweet, Link


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['username', 'email']
    fieldsets = (
        (None, {
            'fields': (
                'email', 'password'
            ),
        }),
        (_('Personal Info'), {
            "fields": ('username',)
        }),
        (_('Permissions'), {
            "fields": ('is_active', 'is_staff', 'is_superuser')
        }),
        (_('Important dates'), {
            "fields": ('last_login',)
        }),
    )

    add_fieldsets = (
        (None, {

            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )


class LinkAdmin(admin.ModelAdmin):
    list_display = ('url', 'tweet')


class TweetAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'tip', 'author', )


admin.site.register(CustomUser, UserAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(Tweet, TweetAdmin)

admin.site.site_header = "Twipee"
admin.site.site_title = "Twipee Official"
admin.site.index_title = "dashboard"
